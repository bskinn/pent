r"""*Mini-language parser for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    8 Sep 2018

**Copyright**
    \(c) Brian Skinn 2018

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
from .enums import NumberMatchType, StringMatchType, AnyMatchType
from .errors import BadTokenError
from .patterns import number_patterns, std_wordify_open, std_wordify_close


# ## MINI-LANGUAGE PARSER DEFINITION ##

# ## HELPERS ##
def _concat_values(e):
    """Concatenate the values of the given Enum."""
    return "".join(_.value for _ in e)


def _has_value(e, v):
    """Check if Enum 'e' has value 'v'."""
    return v in (_.value for _ in e)


group_prefix = "g"

_s_any_flag = "~"

_s_num_no_space = "x"

# ## ARBITRARY CONTENT ##
# Tilde says anything may be here, including multiple words
_pp_any_flag = pp.Literal(_s_any_flag)

# ## LITERAL STRING ##
# Marker for the rest of the token to be a literal string
_pp_str_flag = pp.Word(_concat_values(StringMatchType), exact=1)

# Remainder of the content after the marker, spaces included
_pp_str_content = pp.Word(pp.printables + " ")

# Composite pattern for a literal string
_pp_string = _pp_str_flag + _pp_str_content

# ## NUMERICAL VALUE ##
# Initial marker for a numerical value
_pp_num_flag = pp.Word(_concat_values(NumberMatchType), exact=1)

# Marker for the sign of the value; period indicates either sign
_pp_num_sign = pp.Word(_concat_values(Sign), exact=1)

# Marker for the number type to look for
_pp_num_type = pp.Word(_concat_values(Number), exact=1)

# Composite pattern for a number
_pp_number = (
    _pp_num_flag.setResultsName(TokenField.Type.value)
    + pp.Group(
        _pp_num_sign.setResultsName(TokenField.Sign.value)
        + _pp_num_type.setResultsName(TokenField.Number.value)
    ).setResultsName(TokenField.SignNumber.value)
    + pp.Optional(pp.Literal(_s_num_no_space)).setResultsName(
        TokenField.NoSpace.value
    )
    + pp.WordEnd()
)

# ## COMBINED TOKEN PARSER ##
_pp_token = _pp_any_flag ^ _pp_string ^ _pp_number

# Will (presumably) eventually need to implement preceding/following
# literal strings on the number specifications


# ## PARSER CLASS FOR EXTERNAL USE ##


@attr.s
class Parser:
    """Mini-language parser for structured numerical data."""

    @classmethod
    def convert_line(cls, line, *, capture_groups=True):
        """Implement dirt-oversimple line converter."""
        import shlex

        # Parse line into tokens, and then into Tokens
        tokens = shlex.split(line)
        tokens = list(Token(_, capture=capture_groups) for _ in tokens)

        # Zero-length start of line (or of entire string) match
        pattern = r"(^|(?<=\n))"

        # Always have optional starting whitespace
        pattern += r"[ \t]*"

        # Must initialize
        group_id = 0

        # Initialize flag for a preceding no-space-after num token
        prior_no_space_token = False

        for i, t in enumerate(tokens):
            tok_pattern = t.pattern
            if t.needs_group_id:
                group_id += 1
                tok_pattern = tok_pattern.format(str(group_id))

            if t.is_num:
                if not prior_no_space_token:
                    tok_pattern = std_wordify_open(tok_pattern)

                if t.space_after:
                    tok_pattern = std_wordify_close(tok_pattern)
                    prior_no_space_token = False
                else:
                    prior_no_space_token = True

                pattern += tok_pattern

            else:
                pattern += tok_pattern
                prior_no_space_token = False

            # Add required space or no space, depending on
            # what the token calls for, as long as it's not
            # the last token
            if i < len(tokens) - 1 and t.space_after:
                pattern += r"[ \t]+"

        # Always put possible whitespace to the end of the line
        pattern += r"[ \t]*($|(?=\n))"

        return pattern


@attr.s
class Token:
    """Encapsulates transforming mini-language patterns tokens into regex."""

    from .patterns import number_patterns as _numpats

    #: Mini-language token string to be parsed
    token = attr.ib()

    #: Whether group captures should be added or not
    capture = attr.ib(default=True)

    #: Flag for whether group ID substitution needs to be done
    needs_group_id = attr.ib(default=False, init=False, repr=False)

    #: Compiled regex pattern from the token
    @property
    def pattern(self):
        return self._pattern

    #: Flag for whether the token is an "any content" token
    @property
    def is_any(self):
        return _has_value(AnyMatchType, self._pr[0])

    #: Flag for whether the token matches a literal string
    @property
    def is_str(self):
        return _has_value(StringMatchType, self._pr[0])

    #: Flag for whether the token matches a number
    @property
    def is_num(self):
        return _has_value(NumberMatchType, self._pr[0])

    #: String matching type; |None| if token doesn't match a string
    @property
    def str_match_type(self):
        if self.is_str:
            return StringMatchType(self._pr[0])
        else:
            return None

    #: Number matching type; |None| if token doesn't match a number
    @property
    def num_match_type(self):
        if self.is_num:
            return NumberMatchType(self._pr[0])
        else:
            return None

    #: Number format matched; |None| if token doesn't match a number
    @property
    def number(self):
        if self.is_num:
            return Number(
                self._pr[TokenField.SignNumber.value][TokenField.Number.value]
            )
        else:
            return None

    #: Number sign matched; |None| if token doesn't match a number
    @property
    def sign(self):
        if self.is_num:
            return Sign(
                self._pr[TokenField.SignNumber.value][TokenField.Sign.value]
            )
        else:
            return None

    #: Flag for whether space should be provided for after the match
    @property
    def space_after(self):
        if self.is_num:
            return not TokenField.NoSpace.value in self._pr
        elif self.is_str:
            return True
        else:
            return False

    def __attrs_post_init__(self):
        """Handle automatic creation stuff."""
        try:
            self._pr = _pp_token.parseString(self.token)
        except pp.ParseException as e:
            raise BadTokenError(self.token) from e

        if self.is_any:
            self._pattern = ".*?"

        elif self.is_str:
            self._pattern = self._string_pattern(self._pr[1])

            if self.capture and self._pr[0] == StringMatchType.Capture.value:
                self.needs_group_id = True
                self._pattern = self._group_enclose(self._pattern)

        elif self.is_num:
            self._pattern = self._get_number_pattern(self._pr)

            if self.capture and self._pr[0] == NumberMatchType.Single.value:
                self.needs_group_id = True
                self._pattern = self._group_enclose(self._pattern)

    @staticmethod
    def _string_pattern(s):
        """Create a literal string pattern from `s`."""
        pattern = ""

        for c in s:
            if c in "[\^$.|?*+(){}":
                # Must escape regex special characters
                pattern += "\\" + c
            else:
                pattern += c

        return pattern

    @classmethod
    def _get_number_pattern(cls, parse_result):
        """Return the correct number pattern given the parse result."""
        num = Number(
            parse_result[TokenField.SignNumber.value][TokenField.Number.value]
        )
        sign = Sign(
            parse_result[TokenField.SignNumber.value][TokenField.Sign.value]
        )

        return cls._numpats[num, sign]

    @staticmethod
    def _group_open():
        """Create the opening pattern for a named group.

        This leaves a formatting placeholder for the invoking Parser
        to inject the appropriate group ID.

        """
        return r"(?P<{0}{{0}}>".format(group_prefix)

    @staticmethod
    def _group_close():
        """Create the closing pattern for a named group."""
        return ")"

    @classmethod
    def _group_enclose(cls, pat):
        """Enclose the pattern in the group enclosure."""
        return cls._group_open() + pat + cls._group_close()


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
