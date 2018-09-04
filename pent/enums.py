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


class Number(Enum):
    """Enumeration for the different kinds of recognized number primitives."""

    #: Integer value; no decimal or scientific/exponential notation
    Integer = "int"

    #: Floating-point value; no scientific/exponential notation
    Float = "float"

    #: Scientific/exponential notation, where exponent is *required*
    SciNot = "sci"

    #: "Decimal" value; floating-point value with or without an exponent
    Decimal = "dec"

    #: "General" value; integer, float, or scientific notation
    General = "gen"


class Sign(Enum):
    """Enumeration for the different kinds of recognized numerical signs."""

    #: Positive value only (leading '+' optional; includes zero)
    Positive = "pos"

    #: Negative value only (leading '-' required; includes negative zero)
    Negative = "neg"

    #: Any sign
    Any = "any"
