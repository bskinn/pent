r"""*Regex patterns for* ``pent``.

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

from .enums import Number, Sign


#: |str| with the standard allowed scientific notation exponent
#: marker characters
std_scinot_markers = "deDE"


#: |str| with the standard numerical punctuation to include as not
#: marking word boundaries. `de` is included to account for scientific
#: notation.
std_num_punct = std_scinot_markers + "+.-"  # MUST have '-' at the end!!


#: Standard word marker characters for pent
std_word_chars = "a-zA-Z0-9" + std_num_punct


def wordify_open(p, word_chars):
    """Prepend the word start markers."""
    return r"(?<![{0}]){1}".format(word_chars, p)


def wordify_close(p, word_chars):
    """Append the word end markers."""
    return r"{1}(?![{0}])".format(word_chars, p)


def wordify_pattern(p, word_chars):
    """Wrap pattern with word start/end markers using arbitrary word chars."""
    return wordify_open(wordify_close(p, word_chars), word_chars)


def std_wordify(p):
    """Wrap a token in the ``pent`` standard word start/end markers."""
    return wordify_pattern(p, std_word_chars)


def std_wordify_open(p):
    """Prepend the standard word start markers."""
    return r"(?<![{0}]){1}".format(std_word_chars, p)


def std_wordify_close(p):
    """Append the standard word end markers."""
    return r"{1}(?![{0}])".format(std_word_chars, p)


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


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
