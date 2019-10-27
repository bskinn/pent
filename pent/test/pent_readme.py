r"""``README.rst`` test object for* ``pent`` *test suite*.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    25 Oct 2018

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

import doctest as dt
import os.path as osp
import unittest as ut


def setup_pent_import(dt_obj):
    """Import pent and numpy into the test globals."""
    import pathlib

    import numpy as np

    import pent

    dt_obj.globs.update({"pent": pent, "np": np, "pathlib": pathlib})


TestPentReadme = dt.DocFileSuite(
    osp.abspath("README.rst"),
    module_relative=False,
    setUp=setup_pent_import,
    optionflags=dt.ELLIPSIS,
)


def suite_doctest_readme():
    """Create and return the test suite for README."""
    s = ut.TestSuite()
    s.addTests([TestPentReadme])

    return s
