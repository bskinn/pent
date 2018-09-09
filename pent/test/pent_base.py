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
import re
import unittest as ut

import pyparsing as pp


class TestPentCorePatterns(ut.TestCase):
    """Confirming basic pattern matching of the core pyparsing patterns."""

    @staticmethod
    def parsetest(npat, s):
        """Run an individual parse test on `s` using pattern `npat`."""
        m = re.search(npat, s)

        return m is not None

    @staticmethod
    def make_testname(v, n, s):
        """Compose test name from a numerical value and pattern Number/Sign."""
        return "{0}_{1}_{2}".format(v, n, s)

    def test_number_and_sign_matching(self):
        """Confirm number and sign patterns match the right string patterns."""
        import pent

        from .testdata import number_sign_vals as vals

        for (v, n, s) in itt.product(vals, pent.Number, pent.Sign):
            with self.subTest(self.make_testname(v, n, s)):
                npat = pent.number_patterns[(n, s)]
                npat = pent.std_wordify(npat)

                res = self.parsetest(npat, v)

                self.assertEqual(vals[v][(n, s)], res, msg=npat)

    def test_raw_single_value_space_delimited(self):
        """Confirm single-value parsing works with raw pyparsing patterns."""
        import pent

        from .testdata import number_sign_vals as vals

        test_line = "This line contains the value {} with space delimit."

        for v in vals:
            test_str = test_line.format(v)

            for (n, s) in itt.product(pent.Number, pent.Sign):
                with self.subTest(self.make_testname(v, n, s)):
                    npat = pent.number_patterns[(n, s)]
                    npat = pent.std_wordify(npat)

                    res = self.parsetest(npat, test_str)

                    self.assertEqual(vals[v][(n, s)], res, msg=test_str)


def suite_expect_good():
    """Create and return the test suite for expect-good tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentCorePatterns)])
    return s


if __name__ == "__main__":
    print("Module not executable.")
