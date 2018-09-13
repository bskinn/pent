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
    "Parser",
    "Token",
    "Number",
    "Sign",
    "TokenField",
    "Content",
    "Quantity",
    "number_patterns",
    "wordify_pattern",
    "std_wordify",
    "group_prefix",
    "PentError",
    "BadTokenError",
]

from .enums import Number, Sign, TokenField
from .enums import Content, Quantity
from .errors import PentError, BadTokenError
from .parser import Parser, Token, group_prefix
from .patterns import number_patterns, wordify_pattern, std_wordify


__version__ = "0.1.dev2"
