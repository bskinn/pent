r"""``pyparsing`` *patterns for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    2 Sep 2018

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

import itertools as itt
import re

from .enums import Number, Sign


#: |str| with the standard allowed scientific notation exponent
#: marker characters
std_scinot_markers = "deDE"


#: |str| with the standard numerical punctuation to include as not
#: marking word boundaries. `de` is included to account for scientific
#: notation.
std_num_punct = std_scinot_markers + "+.-"


def wordify_pattern(p, word_chars):
    """Wrap a pattern with word start/end markers using arbitrary word chars."""
    return r"(?<![{0}]){1}(?![{0}])".format(word_chars, p)


def std_wordify(p):
    """Wrap a token in the ``pent`` standard word start/end markers."""
    return wordify_pattern(p, "a-zA-Z0-9" + std_num_punct)


_p_intnums = r"\d+"

_p_floatnums = r"(\d+\.\d*|\d*\.\d+)"

_p_scinums = r"(\d+\.?\d*[{0}][+-]?\d+|\d*\.\d+[{0}][+-]?\d+)".format(
    std_scinot_markers
)

_p_decimalnums = r"({0}|{1})".format(_p_floatnums, _p_scinums)


_p_generalnums = r"({0}|{1}|{2})".format(_p_floatnums, _p_scinums, _p_intnums)


_p_nums = {
    Number.Integer: _p_intnums,
    Number.Float: _p_floatnums,
    Number.SciNot: _p_scinums,
    Number.Decimal: _p_decimalnums,
    Number.General: _p_generalnums,
}

_p_signs = {Sign.Positive: "[+]?", Sign.Negative: "-", Sign.Any: "[+-]?"}

#: |dict| of ``pyparsing`` patterns matching single numbers.
number_patterns = {}

for (n, s) in itt.product(Number, Sign):
    number_patterns.update({(n, s): _p_signs[s] + _p_nums[n]})


if __name__ == "__main__":
    print("Module not executable.")
