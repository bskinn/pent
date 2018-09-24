r"""``Enums`` *for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    3 Sep 2018

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

from enum import Enum


class Number(str, Enum):
    """Enumeration for the different kinds of recognized number primitives."""

    #: Integer value; no decimal or scientific/exponential notation
    Integer = "i"

    #: Floating-point value; no scientific/exponential notation
    Float = "f"

    #: Scientific/exponential notation, where exponent is *required*
    SciNot = "s"

    #: "Decimal" value; floating-point value with or without an exponent
    Decimal = "d"

    #: "General" value; integer, float, or scientific notation
    General = "g"


class Sign(str, Enum):
    """Enumeration for the different kinds of recognized numerical signs."""

    #: Positive value only (leading '+' optional; includes zero)
    Positive = "+"

    #: Negative value only (leading '-' required; includes negative zero)
    Negative = "-"

    #: Any sign
    Any = "."


class Content(str, Enum):
    """Enumeration for the possible types of content."""

    #: Arbitrary match
    Any = "~"

    #: Literal string
    String = "@"

    #: Number
    Number = "#"


class Quantity(str, Enum):
    """Enumeration for the various match quantities."""

    #: Single value match
    Single = "."

    # ~ #: Optional single value match
    # ~ Optional = "?"

    #: One-or-more match
    OneOrMore = "+"

    # ~ #: Zero-or-more match
    # ~ ZeroOrMore = "*"


class TokenField(str, Enum):
    """Enumeration for fields within a mini-language number token."""

    #: Content type (any, string, number)
    Type = "type"

    #: Flag to suppress preceding space in the generated pattern
    NoSpace = "no_space"

    #: Flag to ignore matched content when collecting into regex groups
    Capture = "capture"

    #: Match quantity of the field (single value, optional,
    #: one-or-more, zero-or-more, etc.)
    Quantity = "quantity"

    #: Literal content, for a string match
    Str = "str"

    #: Combined sign and number, for initial pattern group retrieval
    SignNumber = "sign_number"

    #: Format of the numerical value (int, float, scinot, decimal, general)
    Number = "number"

    #: Sign of acceptable values (any, positive, negative)
    Sign = "sign"


class ParserField(str, Enum):
    """Enumeration for the fields/subsections of a Parser pattern."""

    #: Header
    Head = "head"

    #: Body
    Body = "body"

    #: Tail/footer
    Tail = "tail"


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
