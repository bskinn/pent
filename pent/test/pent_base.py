r"""*Test objects for* ``pent`` *test suite*.

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

*(none documented)*

"""


import itertools as itt
import unittest as ut

import pyparsing as pp


class TestPentCorePatterns(ut.TestCase):
    """Confirming basic pattern matching of the core pyparsing patterns."""

    def test_number_and_sign_matching(self):
        """Confirm number and sign patterns match the right string patterns."""
        from pent import Number, Sign
        from pent import number_patterns

        from .testdata import number_sign_vals as vals

        for (v, n, s) in itt.product(vals, Number, Sign):
            testname = "{0}_{1}_{2}".format(v, n, s)
            with self.subTest(testname):
                p = number_patterns[(n, s)]
                try:
                    p.parseString(v)
                except pp.ParseException:
                    res = False
                else:
                    res = True

                self.assertEqual(vals[v][(n, s)], res)


def suite_expect_good():
    """Create and return the test suite for expect-good tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentCorePatterns)])
    return s


if __name__ == "__main__":
    print("Module not executable.")
