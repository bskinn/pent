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
from .patterns import number_patterns, wordify_pattern, std_wordify


# ## MINI-LANGUAGE PARSER DEFINITION ##

# ## HELPERS ##
def _concat_values(e):
    """Concatenate the values of the given Enum."""
    return "".join(_.value for _ in e)

group_prefix = 'g'

_s_any_flag = "~"

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
_pp_number = _pp_num_flag.setResultsName(TokenField.Type.value) + pp.Group(
    _pp_num_sign.setResultsName(TokenField.Sign.value)
    + _pp_num_type.setResultsName(TokenField.Number.value)
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
            pattern += r"\s*" if i == 0 else r"\s+"

            # Will raise parse error here if bad token
            pr = _pp_token.parseString(t)

            if pr[0] == _s_any_flag:
                pattern += ".*?"

            elif pr[0] == StringMatchType.Ignore.value:
                pattern += cls._string_pattern(pr[1])

            elif pr[0] == StringMatchType.Capture.value:
                if capture_groups:
                    group_id += 1
                    pattern += cls._group_open(group_id)

                pattern += cls._string_pattern(pr[1])

                if capture_groups:
                    pattern += cls._group_close()

            elif pr[0] == NumberMatchType.Suppress.value:
                num_pat = cls._get_number_pattern(pr[1])
                pattern += std_wordify(num_pat)

        # Plus possible whitespace to the end of the line
        # THIS APPROACH *MAY* END UP BEING PROBLEMATIC
        pattern += r"[ ]*($|(?=\n))"

        return pattern

    @staticmethod
    def _get_number_pattern(parse_result):
        """Return the correct number pattern given the parse result."""
        num = Number(parse_result[TokenField.Number.value])
        sign = Sign(parse_result[TokenField.Sign.value])

        return number_patterns[num, sign]

    @staticmethod
    def _group_open(group_id):
        """Create the opening pattern for a named group."""
        return r"(?P<g{}>".format(str(group_id))

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
