r"""*'Live data' test objects for* ``pent`` *test suite*.

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

from pent import ParserField

from .pent_base import SuperPent


class TestPentORCALiveData(ut.TestCase, SuperPent):
    """Confirming ORCA output parses as expected."""

    @classmethod
    def get_orca_cas_file(cls):
        """Return the sample ORCA CAS output."""
        return cls.get_file("Cu_CAS.out.gz")

    @classmethod
    def get_orca_opt_file(cls):
        """Return the sample ORCA optimization output."""
        return cls.get_file("MeCl2F_116.out.gz")

    @classmethod
    def get_orca_trj(cls):
        """Return the sample .trj file."""
        return cls.get_file("MeCl2F_21.trj")

    @classmethod
    def get_orca_C2F4_hess(cls):
        """Return the C2F4 .hess file."""
        return cls.get_file("C2F4_01.hess")

    @classmethod
    def get_orca_H2O_hess(cls):
        """Return the H2O .hess file."""
        return cls.get_file("H2O_08.hess")

    def test_orca_hess_freq_parser(self):
        """Confirm 1-D data parser for ORCA freqs works."""
        import pent

        from .testdata import orca_hess_freqs

        head_pattern = ("@.$vibrational_frequencies", "#!.+i")
        body_pattern = "#.+i #!..f"

        # Trivial application of the tail, but serves to check that
        # it works correctly.
        tail_pattern = ("~", "@.$normal_modes", "#!++i")

        freq_parser = pent.Parser(
            head=head_pattern, body=body_pattern, tail=tail_pattern
        )

        data = self.get_orca_C2F4_hess()

        m = re.search(freq_parser.pattern(), data)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(0).count("\n"), 22)

        self.assertEqual(
            freq_parser.capture_struct(data)[ParserField.Head], [["18"]]
        )
        self.assertEqual(
            freq_parser.capture_struct(data)[ParserField.Tail], [["18", "18"]]
        )

        self.assertEqual(freq_parser.capture_body(data), orca_hess_freqs)

    def test_orca_hess_dipders_parser(self):
        """Confirm 2-D single-block data parser for ORCA dipders works."""
        import pent

        from .testdata import orca_hess_dipders

        head_pattern = ("@.$dipole_derivatives", "#.+i")
        body_pattern = "#!+.f"

        freq_parser = pent.Parser(head=head_pattern, body=body_pattern)

        data = self.get_orca_C2F4_hess()

        self.assertEqual(freq_parser.capture_body(data), orca_hess_dipders)

    def test_orca_hess_column_stacked(self):
        """Confirm column stacking works as expected."""
        import pent

        from .testdata import orca_hess_hessian

        prs = pent.Parser(
            head=("@.$hessian", "#.+i"),
            body=pent.Parser(head="#++i", body="#.+i #!+.f"),
        )

        data = self.get_orca_H2O_hess()

        self.assertEqual(
            orca_hess_hessian, pent.column_stack_2d(prs.capture_body(data)[0])
        )

    def test_ORCA_CAS_orbital_ranges(self):
        """Confirm inactive/active/virtual data captures correctly."""
        import pent

        data = self.get_orca_cas_file()

        prs = pent.Parser(
            head="~ '@.orbital ranges:'",
            body="~ #!.+i @.- #!.+i @.( #!.+i @.orbitals)",
            tail="'@.Number of rotation parameters' @+. #!.+i",
        )

        tail_val = [["1799"]]
        body_result = [
            [["0", "14", "15"], ["15", "21", "7"], ["22", "98", "77"]]
        ]

        self.assertEqual(body_result, prs.capture_body(data))
        self.assertEqual(tail_val, prs.capture_struct(data)[ParserField.Tail])

    def test_ORCA_CAS_CI_setup(self):
        """Confirm capture of CI block config data."""
        import pent

        data = self.get_orca_cas_file()

        prs_inner = pent.Parser(
            head=(
                "@.BLOCK #!.+i @.WEIGHT= #!..f",
                "@.Multiplicity @+. #!.+i",
                "@x.#(Config ~ @+. #!.+i",
                "@.#(CSFs) @+. #!.+i",
                "@.#(Roots) @+. #!.+i",
            ),
            body="@x.ROOT= #o.+i @.WEIGHT= #!..f",
            tail="",
        )

        prs_outer = pent.Parser(
            head=("@.CI-STEP:", "~ '@.multiplicity blocks' @+. #!.+i"),
            body=prs_inner,
        )

        with self.subTest("head_outer"):
            head_result = prs_outer.capture_struct(data)[ParserField.Head]
            self.assertEqual([["3"]], head_result)

        with self.subTest("head_inner"):
            head_inner_result = []
            for bdict in prs_outer.capture_struct(data)[ParserField.Body]:
                head_inner_result.append(bdict[ParserField.Head])

            head_inner_expect = [
                [["1", "0.0000", "6", "43", "48", "4"]],
                [["2", "0.0000", "4", "253", "392", "4"]],
                [["3", "1.0000", "2", "393", "784", "4"]],
            ]

            self.assertEqual(head_inner_result, head_inner_expect)

        with self.subTest("body_inner"):
            body_inner_result = []
            for bdict in prs_outer.capture_struct(data)[ParserField.Body]:
                body_inner_result.append(bdict[ParserField.Body])

            body_inner_expect = [
                [["0.000000"], ["0.000000"], ["0.000000"], ["0.000000"]],
                [["0.000000"], ["0.000000"], ["0.000000"], ["0.000000"]],
                [["1.000000"], ["0.000000"], ["0.000000"], ["0.000000"]],
            ]

            self.assertEqual(body_inner_result, body_inner_expect)

        with self.subTest("body_block"):
            body_result = prs_outer.capture_body(data)
            body_expect = [
                [
                    [["0.000000"], ["0.000000"], ["0.000000"], ["0.000000"]],
                    [["0.000000"], ["0.000000"], ["0.000000"], ["0.000000"]],
                    [["1.000000"], ["0.000000"], ["0.000000"], ["0.000000"]],
                ]
            ]

            self.assertEqual(body_result, body_expect)

    def test_ORCA_CAS_state_results(self):
        """Confirm parse of CAS state results is correct."""
        import pent

        from .testdata import orca_cas_states

        data = self.get_orca_cas_file()
        head_expect = [[["1", "6", "4"]], [["2", "4", "4"]], [["3", "2", "4"]]]

        prs_in = pent.Parser(
            head="@.ROOT #x!.+i @.: @.E= #o!..f ~!",
            body="#!.+f @o.[ #x!.+i @.]: #!.+i",
        )

        prs_out = pent.Parser(
            head=(
                "@+-",
                "~ '@.FOR BLOCK' #!.+i @o.MULT= #!.+i @o.NROOTS= #!.+i",
                "@+-",
                "",
            ),
            body=prs_in,
            tail=("", ""),
        )

        self.assertEqual(prs_out.capture_body(data), orca_cas_states)

        head_result = []
        for bdict in prs_out.capture_struct(data):
            head_result.append(bdict[ParserField.Head])

        self.assertEqual(head_result, head_expect)

    def test_ORCA_opt_progress_results(self):
        """Confirm parse of optimization results block."""
        import pent

        data = self.get_orca_opt_file()

        from .testdata import orca_opt_status

        prs = pent.Parser(
            head=(  # body=(
                "@x+- '@x.|Geometry convergence|' @+-",
                "@.Item @.value @.Tolerance @.Converged",
                "@+-",
            ),
            body="~ #!..f #..f ~!",
            tail=(
                "@+.",
                "@.Max(Bonds) #!.+f @.Max(Angles) #!.+f",
                "@.Max(Dihed) #!.+f @.Max(Improp) #!.+f",
                "@+-",
            ),
        )

        self.assertEqual(prs.capture_body(data), orca_opt_status)

    def test_orca_opt_trajectory(self):
        """Confirm multiple-xyz .trj file parsing."""
        import pent

        from .testdata import orca_opt_trajectory

        prs = pent.Parser(head=("#..i", "~"), body="&!. #!+.f")

        data = self.get_orca_trj()

        res = prs.capture_body(data)

        self.assertEqual(res, orca_opt_trajectory)

    def test_ORCA_opt_progress_results_optline(self):
        """Confirm parse of optimization results block using optline."""
        import pent

        data = self.get_orca_opt_file()

        from .testdata import orca_opt_status_optline

        prs = pent.Parser(
            body=(
                "@x+- '@x.|Geometry convergence|' @+-",
                "@.Item @.value @.Tolerance @.Converged",
                "@+-",
                "? '@.Energy change' #!..f #..f ~!",
                "'@.RMS gradient' #!..f #.+f ~!",
                "'@.MAX gradient' #!..f #.+f ~!",
                "'@.RMS step' #!..f #.+f ~!",
                "'@.MAX step' #!..f #.+f ~!",
                "@+.",
                "@.Max(Bonds) #!.+f @.Max(Angles) #!.+f",
                "@.Max(Dihed) #!.+f @.Max(Improp) #!.+f",
                "@+-",
            )
        )

        self.assertEqual(prs.capture_body(data), orca_opt_status_optline)


class TestPentMultiwfnLiveData(ut.TestCase, SuperPent):
    """Confirming Multiwfn output parses as expected."""

    @classmethod
    def get_mwfn_dens_elf(cls):
        """Return mwfn output with integrated density in ELF basins."""
        return cls.get_file("mwfn_dens_elfbasin.txt")

    @classmethod
    def get_mwfn_li_di_elf(cls):
        """Return mwfn output with LI/DI values in ELF basins."""
        return cls.get_file("mwfn_li_di_elfbasin.txt")

    def test_mwfn_li_data(self):
        """Confirm LI data parses as expected."""
        import pent

        from .testdata import mwfn_li_data

        data = self.get_mwfn_li_di_elf()

        prs = pent.Parser(head="'@.Total localization index:'", body="&!+")

        res = list(
            _
            for _ in itt.chain.from_iterable(prs.capture_body(data)[0])
            if ":" not in _
        )

        self.assertEqual(res, mwfn_li_data)

    def test_mwfn_di_data(self):
        """Confirm DI data parses as expected."""
        import pent

        from .testdata import mwfn_di_data

        data = self.get_mwfn_li_di_elf()

        prs = pent.Parser(
            head="@+* &. @.delocalization ~",
            body=pent.Parser(head="#++i", body="#.+i #!++f"),
        )

        res = pent.column_stack_2d(prs.capture_body(data)[0])

        self.assertEqual(res, mwfn_di_data)

    def test_mwfn_basin_dens_data(self):
        """Confirm integrated basin density data parses as expected."""
        import pent

        from .testdata import mwfn_basin_dens_data

        mwfn_sum_density = [["34.62335750"]]

        data = self.get_mwfn_dens_elf()

        prs = pent.Parser(
            head="@.#Basin @.Integral(a.u.) @.Volume(a.u.^3)",
            body="#.+i #!++f",
            tail="'@.Sum of above values:' #!.+f",
        )

        body = prs.capture_body(data)
        tail = prs.capture_struct(data)[pent.ParserField.Tail]

        with self.subTest("body"):
            self.assertEqual(body, mwfn_basin_dens_data)

        with self.subTest("tail"):
            self.assertEqual(mwfn_sum_density, tail)

    def test_mwfn_attractor_data(self):
        """Confirm attractor/basin data parses as expected."""
        import pent

        from .testdata import mwfn_attractor_data

        mwfn_num_grids = [["85130"]]

        data = self.get_mwfn_dens_elf()

        prs = pent.Parser(
            head=(
                "~ '@.attractors after clustering:'",
                "@.Index '@.Average X,Y,Z' ~ @.Value",
            ),
            body="#.+i #!+.f #!.+f",
            tail="~ '@.interbasin grids:' #!.+i",
        )

        body = prs.capture_body(data)
        tail = prs.capture_struct(data)[pent.ParserField.Tail]

        with self.subTest("body"):
            self.assertEqual(body, mwfn_attractor_data)

        with self.subTest("tail"):
            self.assertEqual(mwfn_num_grids, tail)


class TestPentGAMESSLiveData(ut.TestCase, SuperPent):
    """Confirming GAMESS output parses as expected."""

    @classmethod
    def get_gamess_file(cls):
        """Return GAMESS output file text."""
        return cls.get_file("isosorbide_NO3_02.out.gz")

    def test_gamess_geometry(self):
        """Confirm GAMESS geometry parses as expected."""
        import pent

        from .testdata import gamess_geometry

        data = self.get_gamess_file()

        prs = pent.Parser(
            head=(
                "@.ATOM @.ATOMIC '@.COORDINATES (BOHR)'",
                "@.CHARGE @.X @.Y @.Z",
            ),
            body="&!. #!.+f #!+.f",
        )

        self.assertEqual(gamess_geometry, prs.capture_body(data))

    def test_gamess_gradient(self):
        """Confirm GAMESS gradient parses as expected."""
        import pent

        from .testdata import gamess_gradient

        data = self.get_gamess_file()

        prs = pent.Parser(
            head=(
                "@+-",
                "'@.ENERGY GRADIENT'",
                "@+-",
                "",
                "'@.UNITS ARE HARTREE/BOHR' ~",
            ),
            body="#.+i &. #!+.f",
        )

        self.assertEqual(gamess_gradient, prs.capture_body(data))

    def test_gamess_freqs(self):
        """Confirm GAMESS frequencies list parses as expected."""
        import pent

        from .testdata import gamess_freqs

        data = self.get_gamess_file()

        prs = pent.Parser(
            head=(
                "'@.REFERENCE ON SAYVETZ' ~",
                "",
                "'@.NOTE - THE MODES' ~",
                "'@.SUM ON I' ~",
                "",
                "'@.MODE FREQ(CM**-1)' ~",
            ),
            body="#.+i #!..f &. #+.f",
        )

        self.assertEqual(gamess_freqs, prs.capture_body(data))

    def test_gamess_modes(self):
        """Confirm GAMESS normal modes list parses as expected."""
        import pent

        from .testdata import gamess_modes_split

        data = self.get_gamess_file()

        prs = pent.Parser(
            head=("'@.REDUCED MASS:' #+.f", "'@.IR INTENSITY:' #+.f", ""),
            body="~ #!+.f",
        )

        self.assertEqual(gamess_modes_split, prs.capture_body(data))

    def test_gamess_hess(self):
        """Confirm GAMESS hessian parses as expected."""
        import pent

        from .testdata import gamess_hess_split

        data = self.get_gamess_file()

        prs = pent.Parser(
            head=("@+-", "'@.CARTESIAN FORCE CONSTANT MATRIX'", "@+-"),
            body=pent.Parser(
                head=("", "#.+i #.+i", "&. &.", "@.X @.Y @.Z @.X @.Y @.Z"),
                body="~ &o. #o!..f #o!..f #o!..f #o!..f #o!..f #o!..f",
            ),
        )

        self.assertEqual(gamess_hess_split, prs.capture_body(data))


def suite_live_orca():
    """Create and return the test suite for ORCA tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentORCALiveData)])
    return s


def suite_live_mwfn():
    """Create and return the test suite for Multiwfn tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentMultiwfnLiveData)])
    return s


def suite_live_gamess():
    """Create and return the test suite for GAMESS tests."""
    s = ut.TestSuite()
    tl = ut.TestLoader()
    s.addTests([tl.loadTestsFromTestCase(TestPentGAMESSLiveData)])
    return s


if __name__ == "__main__":
    print("Module not executable.")
