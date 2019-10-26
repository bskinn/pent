r"""*Base package module for* ``pent`` *test suite*.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    2 Sep 2018

**Copyright**
    \(c) Brian Skinn 2018-2019

**Source Repository**
    http://www.github.com/bskinn/pent

**Documentation**
    http://pent.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

*(none documented)*

"""

from __future__ import absolute_import

__all__ = [
    "suite_base",
    "suite_base_slow",
    "suite_live_orca",
    "suite_live_mwfn",
    "suite_live_gamess",
    "suite_doctest_readme",
]

from .pent_base import suite_base
from .pent_livedata import suite_live_orca, suite_live_mwfn, suite_live_gamess
from .pent_readme import suite_doctest_readme
from .pent_slow import suite_base_slow
