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

import pyparsing as pp

from .enums import Number, Sign

#: |str| with the standard numerical punctuation to include as not
#: marking word boundaries. `de` is included to account for scientific
#: notation.
std_num_punct = "+-.de"


def wordify_pattern(p, word_chars):
    """Wrap a pattern with word start/end markers using arbitrary word chars."""
    ws = pp.WordStart(word_chars)
    we = pp.WordEnd(word_chars)

    return pp.Combine(ws + p + we)


def std_wordify(p):
    """Wrap a token in the ``pent`` standard word start/end markers."""
    return wordify_pattern(p, pp.nums + std_num_punct)


#: |dict| of ``pyparsing`` patterns matching single numbers.
number_patterns = {
    (Number.Integer, Sign.Positive): pp.Combine(
        pp.Optional("+") + pp.Word(pp.nums)
    ),
    (Number.Integer, Sign.Negative): pp.Combine(
        pp.Literal("-") + pp.Word(pp.nums)
    ),
    (Number.Integer, Sign.Any): pp.Combine(
        pp.Optional(pp.Literal("-") ^ pp.Literal("+")) + pp.Word(pp.nums)
    ),
}

# pyparsing patterns from initial work. Definitely remove the .WordStart
# and .WordEnd tokens from these core definitions.

# ~ # Integers (code i)
# ~ strs.update({Values.POSINT: '[+]?\\d+'})
# ~ strs.update({Values.NEGINT: '-\\d+'})
# ~ strs.update({Values.ANYINT: '[-+]?\\d+'})

# ~ # Floats (code f)
# ~ strs.update({Values.POSFLOAT: '[+]?(\\d+\\.\\d*|\\d*\\.\\d+)'})
# ~ strs.update({Values.NEGFLOAT: '-(\\d+\\.\\d*|\\d*\\.\\d+)'})
# ~ strs.update({Values.ANYFLOAT: '[-+]?(\\d+\\.\\d*|\\d*\\.\\d+)'})

# ~ # Scinot (code s; accepts both d and e for the exponent marker)
# ~ strs.update({Values.POSSCI: '[+]?(\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})
# ~ strs.update({Values.NEGSCI: '-(\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})
# ~ strs.update({Values.ANYSCI: '[-+]?(\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})

# ~ # Float or scinot (code d, for ... decimal?)
# ~ strs.update({Values.POSDEC: '[+]?(\\d+\\.\\d*|\\d*\\.\\d+|\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})
# ~ strs.update({Values.NEGDEC: '-(\\d+\\.\\d*|\\d*\\.\\d+|\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[dDEe][-+]?\\d+)'})
# ~ strs.update({Values.ANYDEC: '[-+]?(\\d+\\.\\d*|\\d*\\.\\d+|\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})

# ~ # Any numerical value (code n)
# ~ # This one is simpler than decimal because the first pattern option of the two matches integers (everything
# ~ #  after the initial `\\d+` is optional)
# ~ strs.update({Values.POSNUM: '[+]?(\\d+\\.?\\d*([deDE][-+]?\\d+)?|\\d*\\.\\d+([deDE][-+]?\\d+)?)'})
# ~ strs.update({Values.NEGNUM: '-(\\d+\\.?\\d*([deDE][-+]?\\d+)?|\\d*\\.\\d+([deDE][-+]?\\d+)?)'})
# ~ strs.update({Values.ANYNUM: '[-+]?(\\d+\\.?\\d*([deDE][-+]?\\d+)?|\\d*\\.\\d+([deDE][-+]?\\d+)?)'})


if __name__ == "__main__":
    print("Module not executable.")
