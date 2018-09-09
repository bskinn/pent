r"""*Core package definition module for* ``pent``.

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


from __future__ import absolute_import

__all__ = [
    "Number",
    "Sign",
    "number_patterns",
    "wordify_pattern",
    "std_wordify",
]

from .enums import Number, Sign
from .patterns import number_patterns, wordify_pattern, std_wordify


__version__ = "0.1dev1"
