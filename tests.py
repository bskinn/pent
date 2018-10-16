r"""*Master script for* ``pent`` *test suite*.

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


class AP(object):
    """ Container for arguments for selecting test suites.

    Also includes PFX, a helper string for substitution/formatting.

    """

    ALL = "all"

    FAST = "fast"

    LIVE = "live"
    ORCA = "orca"
    MWFN = "mwfn"

    PFX = "--{0}"


def get_parser():
    import argparse

    # Create the parser
    prs = argparse.ArgumentParser(description="Run tests for pent")

    # Verbosity argument
    prs.add_argument("-v", action="store_true", help="Show verbose output")

    # Test subgroups
    grp_livedata = prs.add_argument_group(title="Run live-data tests")

    # Options without subgroups
    prs.add_argument(
        AP.PFX.format(AP.ALL),
        "-a",
        action="store_true",
        help="Run all tests (overrides any other selections)",
    )
    prs.add_argument(
        AP.PFX.format(AP.FAST),
        "-f",
        action="store_true",
        help="Run only 'fast' tests",
    )

    # Subgroup for live data
    grp_livedata.add_argument(
        AP.PFX.format(AP.LIVE),
        "-l",
        action="store_true",
        help="Run all 'live data' tests",
    )
    grp_livedata.add_argument(
        AP.PFX.format(AP.ORCA),
        action="store_true",
        help="Run all ORCA 'live data' tests",
    )
    grp_livedata.add_argument(
        AP.PFX.format(AP.MWFN),
        action="store_true",
        help="Run all Multiwfn 'live data' tests",
    )

    # Return the parser
    return prs


def main():
    import sys
    import unittest as ut

    import pent.test

    # Retrieve the parser
    prs = get_parser()

    # Pull the dict of stored flags, saving the un-consumed args, and
    # update sys.argv
    ns, args_left = prs.parse_known_args()
    params = vars(ns)
    sys.argv = sys.argv[:1] + args_left

    # Create the empty test suite
    ts = ut.TestSuite()

    # Helper function for adding test suites. Just uses ts and params from
    # the main() function scope
    def addsuiteif(suite, flags):
        if any(params[k] for k in flags):
            ts.addTest(suite)

    # Add commandline-indicated tests per-group
    # Fast tests
    addsuiteif(pent.test.pent_base.suite_base(), [AP.ALL, AP.FAST])

    # Slow tests
    addsuiteif(pent.test.pent_slow.suite_base_slow(), [AP.ALL])

    # Live data tests
    addsuiteif(
        pent.test.pent_livedata.suite_live_orca(),
        [AP.ALL, AP.FAST, AP.LIVE, AP.ORCA],
    )
    addsuiteif(
        pent.test.pent_livedata.suite_live_mwfn(),
        [AP.ALL, AP.FAST, AP.LIVE, AP.MWFN],
    )

    # Create the test runner and execute
    ttr = ut.TextTestRunner(buffer=True, verbosity=(2 if params["v"] else 1))
    success = ttr.run(ts).wasSuccessful()

    # Return based on success result (lets tox report success/fail)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
