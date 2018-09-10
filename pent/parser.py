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
from .enums import NumberMatchType, StringMatchType
from .patterns import number_patterns, std_wordify


# ## MINI-LANGUAGE PARSER DEFINITION ##

# ## HELPERS ##
def _concat_values(e):
    """Concatenate the values of the given Enum."""
    return "".join(_.value for _ in e)


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

        tokens = shlex.split(line)

        # Zero-length start of line (or of entire string) match
        pattern = r"(^|(?<=\n))"

        group_id = 0

        for i, t in enumerate(tokens):
            # Optional whitespace before the first token;
            # mandatory whitespace before all others
            pre_space = r"\s*" if i == 0 else r"\s+"

            # Will raise parse error here if bad token
            pr = _pp_token.parseString(t)

            if pr[0] == _s_any_flag:
                pattern += pre_space + ".*?"

            elif pr[0] == StringMatchType.Ignore.value:
                pattern += pre_space + cls._string_pattern(pr[1])

            elif pr[0] == StringMatchType.Capture.value:
                subpat, group_id = cls._group_enclose(
                    cls._string_pattern(pr[1]),
                    group_id,
                    do_enclose=capture_groups,
                )
                pattern += pre_space + subpat

            elif pr[0] == NumberMatchType.Suppress.value:
                # THE 'NO-SPACE BEFORE' FEATURE IS GOING TO BE COMPLEX, SINCE
                # IT WON'T WORK TO WORDIFY THE PATTERNS FROM EACH TOKEN
                # BECAUSE THERE'S NO ACTUAL WORD BREAK WHEN THERE'S NO
                # PRECEDING SPACE
                pattern += "" if TokenField.NoSpace.value in pr else pre_space
                pattern += std_wordify(
                    cls._get_number_pattern(pr[TokenField.SignNumber.value])
                )

            elif pr[0] == NumberMatchType.Single.value:
                subpat, group_id = cls._group_enclose(
                    cls._get_number_pattern(pr[1]),
                    group_id,
                    do_enclose=capture_groups,
                )
                pattern += pre_space + std_wordify(subpat)

        # Plus possible whitespace to the end of the line
        # THIS APPROACH *MAY* END UP BEING PROBLEMATIC
        pattern += r"[ \t]*($|(?=\n))"

        return pattern

    @staticmethod
    def _get_number_pattern(parse_result):
        """Return the correct number pattern given the parse result."""
        num = Number(parse_result[TokenField.Number.value])
        sign = Sign(parse_result[TokenField.Sign.value])

        return number_patterns[num, sign]

    @classmethod
    def _group_enclose(cls, pat, group_id, *, do_enclose=True):
        """Enclose the pattern in the group, if told to do so.

        Returns the pattern, modified or not, and the updated group_id.

        """
        outpat = ""
        if do_enclose:
            group_id += 1
            outpat += cls._group_open(group_id)

        outpat += pat

        if do_enclose:
            outpat += cls._group_close()

        return outpat, group_id

    @staticmethod
    def _group_open(group_id):
        """Create the opening pattern for a named group."""
        return r"(?P<{0}{1}>".format(group_prefix, str(group_id))

    @staticmethod
    def _group_close():
        """Create the closing pattern for a named group."""
        return ")"

    @staticmethod
    def _string_pattern(s):
        """Create a literal string pattern from `s`."""
        pattern = ""

        for c in s:
            if c in "[\^$.|?*+(){}":
                pattern += "\\" + c
            else:
                pattern += c

        return pattern


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
