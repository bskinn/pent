r"""*Token handling for mini-language parser for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    20 Sep 2018

**Copyright**
    \(c) Brian Skinn 2018-2019

**Source Repository**
    http://www.github.com/bskinn/pent

**Documentation**
    http://pent.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import attr
import pyparsing as pp

from .enums import Number, Sign, TokenField
from .enums import Content, Quantity, SpaceAfter
from .errors import TokenError


@attr.s(slots=True)
class Token:
    """Encapsulates transforming mini-language patterns tokens into regex."""

    from .patterns import number_patterns as _numpats

    #: Mini-language token string to be parsed
    token = attr.ib()

    #: Whether group capture should be added or not
    do_capture = attr.ib(default=True)

    #: Flag for whether group ID substitution needs to be done
    needs_group_id = attr.ib(default=False, init=False, repr=False)

    # Internal pyparsing parse result and generated regex pattern
    _pr = attr.ib(default=None, init=False, repr=False)
    _pattern = attr.ib(default=None, init=False, repr=False)

    # #####  pyparsing pattern internals #####

    # ## MINOR PATTERN COMPONENTS ##
    group_prefix = "g"
    _s_any_flag = "~"
    _s_capture = "!"

    _pp_space_after = pp.Optional(
        pp.Word("".join(SpaceAfter), exact=1)
    ).setResultsName(TokenField.SpaceAfter)
    _pp_capture = pp.Optional(pp.Literal(_s_capture)).setResultsName(
        TokenField.Capture
    )
    _pp_quantity = pp.Word("".join(Quantity), exact=1).setResultsName(
        TokenField.Quantity
    )

    # ## OPTIONAL LINE TOKEN ##
    _pp_optional_line = pp.Literal(Content.OptionalLine.value).setResultsName(
        TokenField.Type
    )

    # ## ARBITRARY CONTENT TOKEN ##
    # Anything may be matched here, including multiple words.
    _pp_any_flag = (
        pp.Literal(_s_any_flag).setResultsName(TokenField.Type) + _pp_capture
    )

    # ## LITERAL STRING TOKEN ##
    # Marker for the rest of the token to be a literal string
    _pp_str_flag = pp.Literal(Content.String.value).setResultsName(
        TokenField.Type
    )

    # Remainder of the content after the marker, spaces included
    _pp_str_value = pp.Word(pp.printables + " ").setResultsName(TokenField.Str)

    # Composite pattern for a literal string
    _pp_string = (
        _pp_str_flag
        + _pp_space_after
        + _pp_capture
        + _pp_quantity
        + _pp_str_value
    )

    # ## MISC SINGLE VALUE TOKEN ##
    # Initial marker for the 'misc' token
    _pp_misc_flag = pp.Literal(Content.Misc.value).setResultsName(
        TokenField.Type
    )

    # Composite token pattern for the misc match
    _pp_misc = _pp_misc_flag + _pp_space_after + _pp_capture + _pp_quantity

    # ## NUMERICAL VALUE TOKEN ##
    # Initial marker for a numerical value
    _pp_num_flag = pp.Literal(Content.Number.value).setResultsName(
        TokenField.Type
    )

    # Marker for the sign of the value; period indicates either sign
    _pp_num_sign = pp.Word("".join(Sign), exact=1).setResultsName(
        TokenField.Sign
    )

    # Marker for the number type to look for
    _pp_num_type = pp.Word("".join(Number), exact=1).setResultsName(
        TokenField.Number
    )

    # Composite pattern for a number
    _pp_number = (
        _pp_num_flag
        + _pp_space_after
        + _pp_capture
        + _pp_quantity
        + pp.Group(_pp_num_sign + _pp_num_type).setResultsName(
            TokenField.SignNumber
        )
    )

    # ## COMBINED TOKEN PARSER ##
    _pp_token = (
        pp.StringStart()
        + (
            _pp_optional_line
            ^ _pp_any_flag
            ^ _pp_string
            ^ _pp_number
            ^ _pp_misc
        )
        + pp.StringEnd()
    )

    # Informational properties
    @property
    def pattern(self):
        """Return assembled regex pattern from the token, as |str|."""
        return self._pattern

    @property
    def is_any(self):
        """Return flag for whether the token is an "any content" token."""
        return self._pr[TokenField.Type] == Content.Any

    @property
    def is_optional_line(self):
        """Return flag for whether the token flags an optional line."""
        return self._pr[TokenField.Type] == Content.OptionalLine

    @property
    def is_str(self):
        """Return flag for whether the token matches a literal string."""
        return self._pr[TokenField.Type] == Content.String

    @property
    def is_misc(self):
        """Return flag for whether the token is a misc token."""
        return self._pr[TokenField.Type] == Content.Misc

    @property
    def is_num(self):
        """Return flag for whether the token matches a number."""
        return self._pr[TokenField.Type] == Content.Number

    @property
    def match_quantity(self):
        """Return match quantity.

        |None| for :attr:`pent.enums.Content.Any` or
        :attr:`pent.enums.Content.OptionalLine`

        """
        if self.is_any or self.is_optional_line:
            return None
        else:
            return Quantity(self._pr[TokenField.Quantity])

    @property
    def number(self):
        """#: Return number format; |None| if token doesn't match a number."""
        if self.is_num:
            return Number(self._pr[TokenField.SignNumber][TokenField.Number])
        else:
            return None

    @property
    def sign(self):
        """#: Return number sign; |None| if token doesn't match a number."""
        if self.is_num:
            return Sign(self._pr[TokenField.SignNumber][TokenField.Sign])
        else:
            return None

    @property
    def space_after(self):
        """Return Enum value for handling of post-match whitespace."""
        if self.is_any:
            return False
        elif TokenField.SpaceAfter in self._pr:
            return SpaceAfter(self._pr[TokenField.SpaceAfter])
        else:
            return SpaceAfter.Required

    @property
    def capture(self):
        """Return flag for whether a regex capture group should be created."""
        return TokenField.Capture in self._pr

    def __attrs_post_init__(self):
        """Handle automatic creation stuff."""
        try:
            self._pr = self._pp_token.parseString(self.token)
        except pp.ParseException as e:
            raise TokenError(self.token) from e

        if self.is_any:
            self._pattern, self.needs_group_id = self._selective_group_enclose(
                ".*?"
            )
            return

        # Only single and one-or-more captures implemented for now.
        # Optional and zero-or-more captures may actually not be feasible
        if self.is_str:
            # Always store the string pattern
            self._pattern = self._string_pattern()

            # Modify, depending on the Quantity
            if self.match_quantity is Quantity.OneOrMore:
                self._pattern = "(" + self._pattern + ")+"

        elif self.is_num:
            self._pattern = self._get_number_pattern()

            if self.match_quantity is Quantity.OneOrMore:
                self._pattern += r"([ \t]+{})*".format(self._pattern)

        elif self.is_misc:
            self._pattern = self._get_misc_pattern()

            if self.match_quantity is Quantity.OneOrMore:
                self._pattern += r"([ \t]+{})*".format(self._pattern)

        elif self.is_optional_line:
            pass

        else:  # pragma: no cover
            raise NotImplementedError(
                "Unknown content type somehow specified!"
            )

        self._pattern, self.needs_group_id = self._selective_group_enclose(
            self._pattern
        )

    def _string_pattern(self):
        """Create a literal string pattern from the parse result."""
        pattern = ""

        for c in self._pr[TokenField.Str]:
            if c in r"[\^$.|?*+(){}":
                # Must escape regex special characters
                pattern += "\\" + c
            else:
                pattern += c

        return pattern

    def _get_misc_pattern(self):
        """Return the no-whitespace item pattern.

        Lazy capture is probably the best approach here, for
        optional-space after situations?
        That way, it will be as generous as possible in not
        aggressively consuming negative signs on following
        numeric fields, but should still expand to whatever
        extent necessary to cover the whole misc field.

        """
        return r"[^ \t\n]+?"

    def _get_number_pattern(self):
        """Return the correct number pattern given the parse result."""
        num = Number(self._pr[TokenField.SignNumber][TokenField.Number])
        sign = Sign(self._pr[TokenField.SignNumber][TokenField.Sign])

        return self._numpats[num, sign]

    @classmethod
    def _group_open(cls):
        """Create the opening pattern for a named group.

        This leaves a formatting placeholder for the invoking Parser
        to inject the appropriate group ID.

        """
        return r"(?P<{0}{{0}}>".format(cls.group_prefix)

    @staticmethod
    def _group_close():
        """Create the closing pattern for a named group."""
        return ")"

    def _selective_group_enclose(self, pat):
        """Return token pattern enclosed in group IF it should be grouped.

        FIX THIS DOCSTRING, IT'S OUT OF DATE!!!

        """
        if self.do_capture and self.capture:
            return (self._group_open() + pat + self._group_close(), True)
        else:
            return pat, False
