r"""*SLOW test objects for* ``pent`` *test suite*.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    9 Oct 2018

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

from .pent_base import SuperPent


class TestPentParserPatternsSlow(ut.TestCase, SuperPent):
    """SLOW tests confirming pattern matching of Parser regexes."""

    import pent

    prs = pent.Parser(body="")

    def test_three_token_sequence(self):
        """Ensure combinatorial token sequence parses correctly."""
        import pent

        from .testdata import number_patterns as nps

        pat_template = "~ {0} {1} {2} ~"
        str_template = "String! {0}{1}{2}{3}{4} More String!"
        str_pat = {"foo": "@{0}{1}{2}foo"}

        testname_template = "{0}_{1}_{2}_{3}_{4}"

        str_or_num = (pent.Content.String, pent.Content.Number)
        t_f = (True, False)

        for c1, s1, c2, s2, c3 in itt.product(
            str_or_num, t_f, str_or_num, t_f, str_or_num
        ):
            if (c1 is c2 and not s1) or (c2 is c3 and not s2):
                # No reason to have no-space strings against one another;
                # no-space numbers adjacent to one another make
                # no syntactic sense.
                continue

            vals1 = str_pat if c1 == pent.Content.String else nps.keys()
            vals2 = str_pat if c2 == pent.Content.String else nps.keys()
            vals3 = str_pat if c3 == pent.Content.String else nps.keys()

            for v1, v2, v3 in itt.product(vals1, vals2, vals3):
                p1 = (str_pat if c1 == pent.Content.String else nps)[
                    v1
                ].format(
                    pent.SpaceAfter.Prohibited if not s1 else "",
                    pent.Token._s_capture,
                    pent.Quantity.Single,
                )
                p2 = (str_pat if c2 == pent.Content.String else nps)[
                    v2
                ].format(
                    pent.SpaceAfter.Prohibited if not s2 else "",
                    pent.Token._s_capture,
                    pent.Quantity.Single,
                )
                p3 = (str_pat if c3 == pent.Content.String else nps)[
                    v3
                ].format("", pent.Token._s_capture, pent.Quantity.Single)

                test_pat = pat_template.format(p1, p2, p3)
                test_str = str_template.format(
                    v1, " " if s1 else "", v2, " " if s2 else "", v3
                )

                with self.subTest(
                    testname_template.format(v1, s1, v2, s2, v3)
                ):
                    npat = self.prs.convert_line(test_pat)[0]

                    m = re.search(npat, test_str)

                    self.assertIsNotNone(m, msg=test_pat)
                    self.assertEqual(
                        m.group(pent.Token.group_prefix + "0"),
                        v1,
                        msg=test_pat + " :: " + test_str,
                    )
                    self.assertEqual(
                        m.group(pent.Token.group_prefix + "1"),
                        v2,
                        msg=test_pat + " :: " + test_str,
                    )
                    self.assertEqual(
                        m.group(pent.Token.group_prefix + "2"),
                        v3,
                        msg=test_pat + " :: " + test_str,
                    )


def suite_base_slow():
    """Create and return the test suite for SLOW base tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentParserPatternsSlow)])
    return s


if __name__ == "__main__":
    print("Module not executable.")
