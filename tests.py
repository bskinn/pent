# ------------------------------------------------------------------------------
# Name:        tests
# Purpose:     Master script for pent testing suite
#
# Author:      Brian Skinn
#                bskinn@alum.mit.edu
#
# Created:     2 Sep 2018
# Copyright:   (c) Brian Skinn 2018
# License:     The MIT License; see "LICENSE.txt" for full license terms.
#
#           http://www.github.com/bskinn/pent
#
# ------------------------------------------------------------------------------


class AP(object):
    """ Container for arguments for selecting test suites.

    Also includes PFX, a helper string for substitution/formatting.

    """
    ALL = 'all'

    PFX = "--{0}"


def get_parser():
    import argparse

    # Create the parser
    prs = argparse.ArgumentParser(description="Run tests for pent")

    # Verbosity argument
    prs.add_argument('-v', action='store_true',
                     help="Show verbose output")

    # Test subgroups

    # Options without subgroups
    prs.add_argument(AP.PFX.format(AP.ALL), '-a',
                     action='store_true',
                     help="Run all tests (overrides any other selections)")

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
    # Expect-good tests
    addsuiteif(pent.test.pent_base.suite_expect_good(),
               [AP.ALL])

#    addsuiteif(sphobjinv.test.sphobjinv_api.suite_api_expect_good(),
#               [AP.ALL, AP.LOCAL, AP.GOOD, AP.GOOD_LOCAL,
#                AP.API, AP.API_LOCAL, AP.API_GOOD, AP.API_GOOD_LOCAL])
#    addsuiteif(sphobjinv.test.sphobjinv_api.suite_api_expect_good_nonlocal(),
#               [AP.ALL, AP.GOOD, AP.API, AP.API_GOOD])
#    addsuiteif(sphobjinv.test.sphobjinv_cli.suite_cli_expect_good(),
#               [AP.ALL, AP.LOCAL, AP.GOOD, AP.GOOD_LOCAL,
#                AP.CLI, AP.CLI_LOCAL, AP.CLI_GOOD, AP.CLI_GOOD_LOCAL])
#    addsuiteif(sphobjinv.test.sphobjinv_cli.suite_cli_expect_good_nonlocal(),
#               [AP.ALL, AP.GOOD, AP.CLI, AP.CLI_GOOD])

#    # Expect-fail tests
#    addsuiteif(sphobjinv.test.sphobjinv_api.suite_api_expect_fail(),
#               [AP.ALL, AP.LOCAL, AP.FAIL, AP.API, AP.API_LOCAL, AP.API_FAIL])
#    addsuiteif(sphobjinv.test.sphobjinv_cli.suite_cli_expect_fail(),
#               [AP.ALL, AP.LOCAL, AP.FAIL, AP.FAIL_LOCAL,
#                AP.CLI, AP.CLI_LOCAL, AP.CLI_FAIL, AP.CLI_FAIL_LOCAL])
#    addsuiteif(sphobjinv.test.sphobjinv_cli.suite_cli_expect_fail_nonlocal(),
#               [AP.ALL, AP.FAIL, AP.CLI, AP.CLI_FAIL])

    # Create the test runner and execute
    ttr = ut.TextTestRunner(buffer=True,
                            verbosity=(2 if params['v'] else 1),
                            )
    success = ttr.run(ts).wasSuccessful()

    # Return based on success result (lets tox report success/fail)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
