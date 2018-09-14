r"""*Supporting test data for* ``pent`` *test suite*.

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


from pent import Number, Sign

number_token_template = "#{{0}}{{1}}{{2}}{0}"

number_patterns = {
    "123": number_token_template.format(".i"),
    "-123": number_token_template.format("-i"),
    "+123": number_token_template.format("+i"),
    "0.2": number_token_template.format(".f"),
    "-.285": number_token_template.format("-f"),
    "+315.": number_token_template.format("+f"),
    "3e5": number_token_template.format(".s"),
    "-.13e+5": number_token_template.format("-s"),
    "+3.1e-5": number_token_template.format("+s"),
    ".266": number_token_template.format(".d"),
    "-15.285": number_token_template.format("-d"),
    "+315.185": number_token_template.format("+d"),
    "35": number_token_template.format(".g"),
    "-.13": number_token_template.format("-g"),
    "+3.1e+15": number_token_template.format("+g"),
}

assert len(number_patterns) == 15

number_sign_vals = {
    "0": {
        (Number.Integer, Sign.Positive): True,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-0": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): True,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+0.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-.00": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+35": {
        (Number.Integer, Sign.Positive): True,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "23": {
        (Number.Integer, Sign.Positive): True,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-12": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): True,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    ".12": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "35.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+218.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+.355": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "0.23": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-.22": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "-234.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "-392.34": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+3e3": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+3e+3": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+3e+003": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "3e+003": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+3.e5": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+2e-04": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+.34e23": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+.48e-2": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-2e-04": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): True,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+-0.39": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): False,
    },
    # INVALID VALUES... complex(?), etc.
}