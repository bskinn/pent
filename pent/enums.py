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


class AnyMatchType(str, Enum):
    """Enumeration for various 'any' match types."""

    #: Non-captured match
    Ignore = "~"


class StringMatchType(str, Enum):
    """Enumeration for the various match types on literal string fields."""

    #: Captured match
    Capture = "="

    #: Ignored match
    Ignore = "!"


class NumberMatchType(str, Enum):
    """Enumeration for the various match types on the numeric fields."""

    #: Single value match
    Single = "."

    #: Optional single value match
    Optional = "?"

    #: One-or-more match
    OneOrMore = "+"

    #: Zero-or-more match
    ZeroOrMore = "*"

    #: Suppressed match
    Suppress = "#"


class TokenField(str, Enum):
    """Enumeration for fields within a mini-language number token."""

    #: Type of number field (single value, one-or-more, zero-or-more, etc.)
    Type = "type"

    #: Sign of acceptable values (any, positive, negative)
    Sign = "sign"

    #: Format of the numerical value (int, float, scinot, decimal, general)
    Number = "number"

    #: Combined sign and number, for initial pattern group retrieval
    SignNumber = "sign_number"

    #: Flag to suppress preceding space in the generated pattern
    NoSpace = "no_space"


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
