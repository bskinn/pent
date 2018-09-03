# ------------------------------------------------------------------------------
# Name:        pent_base
# Purpose:     Module defining common objects for pent tests
#
# Author:      Brian Skinn
#                bskinn@alum.mit.edu
#
# Created:     2 Sep 2018
# Copyright:   (c) Brian Skinn 2018
# License:     The MIT License; see "LICENSE.txt" for full license terms.
#
#            https://www.github.com/bskinn/pent
#
# ------------------------------------------------------------------------------

"""Module defining common objects for pent tests."""


import os
import os.path as osp
import unittest as ut


class TestPentCorePatterns(ut.TestCase):
    """Confirming basic pattern matching of the core pyparsing patterns."""

    def test_dummy_test(self):
        self.assertTrue(True)

# Test content from Jupyter testing

#~ # Set of all test values
#~ vals = {'0': {
                #~ Values.POSINT: True, Values.NEGINT: False, Values.ANYINT: True,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: False, Values.ANYDEC: False,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '-0': {
                #~ Values.POSINT: False, Values.NEGINT: True, Values.ANYINT: True,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: False, Values.ANYDEC: False,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ },
        #~ '+0.': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: True, Values.NEGFLOAT: False, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '-.00': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: True, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: True, Values.ANYDEC: True,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ },
        #~ '+35': {
                #~ Values.POSINT: True, Values.NEGINT: False, Values.ANYINT: True,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: False, Values.ANYDEC: False,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '23': {
                #~ Values.POSINT: True, Values.NEGINT: False, Values.ANYINT: True,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: False, Values.ANYDEC: False,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '-12': {
                #~ Values.POSINT: False, Values.NEGINT: True, Values.ANYINT: True,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: False, Values.ANYDEC: False,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ },
        #~ '.12': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: True, Values.NEGFLOAT: False, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '35.': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: True, Values.NEGFLOAT: False, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+218.': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: True, Values.NEGFLOAT: False, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+.355': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: True, Values.NEGFLOAT: False, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '0.23': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: True, Values.NEGFLOAT: False, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '-.22': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: True, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: True, Values.ANYDEC: True,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ },
        #~ '-234.': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: True, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: True, Values.ANYDEC: True,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ },
        #~ '-392.34': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: True, Values.ANYFLOAT: True,
                #~ Values.POSSCI: False, Values.NEGSCI: False, Values.ANYSCI: False,
                #~ Values.POSDEC: False, Values.NEGDEC: True, Values.ANYDEC: True,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ },
        #~ '+3e3': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+3e+3': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+3e+003': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '3e+003': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+3.e5': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+2e-04': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+.34e23': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '+.48e-2': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: True, Values.NEGSCI: False, Values.ANYSCI: True,
                #~ Values.POSDEC: True, Values.NEGDEC: False, Values.ANYDEC: True,
                #~ Values.POSNUM: True, Values.NEGNUM: False, Values.ANYNUM: True
                #~ },
        #~ '-2e-04': {
                #~ Values.POSINT: False, Values.NEGINT: False, Values.ANYINT: False,
                #~ Values.POSFLOAT: False, Values.NEGFLOAT: False, Values.ANYFLOAT: False,
                #~ Values.POSSCI: False, Values.NEGSCI: True, Values.ANYSCI: True,
                #~ Values.POSDEC: False, Values.NEGDEC: True, Values.ANYDEC: True,
                #~ Values.POSNUM: False, Values.NEGNUM: True, Values.ANYNUM: True
                #~ }
        #~ # INVALID VALUES... '+-0.349', complex(?), etc.
       #~ }


def suite_expect_good():
    """Create and return the test suite for expect-good tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentCorePatterns)])
    return s


if __name__ == '__main__':
    print("Module not executable.")
