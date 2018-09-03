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


class Numbers:
    """Patterns matching single numbers."""

    pass

# pyparsing patterns from initial work. Definitely remove the .WordStart
# and .WordEnd tokens from these core definitions.

#~ ppps = {}
#~ num_punct = '+-.'
#~ ppps.update({Values.POSINT: pp.Combine(pp.WordStart(pp.alphanums + num_punct) +
                                       #~ pp.Optional('+') +
                                       #~ pp.Word(pp.nums) +
                                       #~ pp.WordEnd(pp.alphanums + num_punct))})
#~ ppps.update({Values.NEGINT: pp.Combine(pp.WordStart(pp.alphanums + num_punct) +
                                       #~ pp.Literal('-') +
                                       #~ pp.Word(pp.nums) +
                                       #~ pp.WordEnd(pp.alphanums + num_punct))})
#~ ppps.update({Values.ANYINT: pp.Combine(pp.WordStart(pp.alphanums + num_punct) +
                                       #~ pp.Optional(pp.Literal('+') ^ pp.Literal('-')) +
                                       #~ pp.Word(pp.nums) +
                                       #~ pp.WordEnd(pp.alphanums + num_punct))})

# Regex patterns from initial work:

#~ # Integers (code i)
#~ strs.update({Values.POSINT: '[+]?\\d+'})
#~ strs.update({Values.NEGINT: '-\\d+'})
#~ strs.update({Values.ANYINT: '[-+]?\\d+'})

#~ # Floats (code f)
#~ strs.update({Values.POSFLOAT: '[+]?(\\d+\\.\\d*|\\d*\\.\\d+)'})
#~ strs.update({Values.NEGFLOAT: '-(\\d+\\.\\d*|\\d*\\.\\d+)'})
#~ strs.update({Values.ANYFLOAT: '[-+]?(\\d+\\.\\d*|\\d*\\.\\d+)'})

#~ # Scinot (code s; accepts both d and e for the exponent marker)
#~ strs.update({Values.POSSCI: '[+]?(\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})
#~ strs.update({Values.NEGSCI: '-(\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})
#~ strs.update({Values.ANYSCI: '[-+]?(\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})

#~ # Float or scinot (code d, for ... decimal?)
#~ strs.update({Values.POSDEC: '[+]?(\\d+\\.\\d*|\\d*\\.\\d+|\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})
#~ strs.update({Values.NEGDEC: '-(\\d+\\.\\d*|\\d*\\.\\d+|\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[dDEe][-+]?\\d+)'})
#~ strs.update({Values.ANYDEC: '[-+]?(\\d+\\.\\d*|\\d*\\.\\d+|\\d+\\.?\\d*[deDE][-+]?\\d+|\\d*\\.\\d+[deDE][-+]?\\d+)'})

#~ # Any numerical value (code n)
#~ # This one is simpler than decimal because the first pattern option of the two matches integers (everything
#~ #  after the initial `\\d+` is optional)
#~ strs.update({Values.POSNUM: '[+]?(\\d+\\.?\\d*([deDE][-+]?\\d+)?|\\d*\\.\\d+([deDE][-+]?\\d+)?)'})
#~ strs.update({Values.NEGNUM: '-(\\d+\\.?\\d*([deDE][-+]?\\d+)?|\\d*\\.\\d+([deDE][-+]?\\d+)?)'})
#~ strs.update({Values.ANYNUM: '[-+]?(\\d+\\.?\\d*([deDE][-+]?\\d+)?|\\d*\\.\\d+([deDE][-+]?\\d+)?)'})


if __name__ == '__main__':
    print("Module not executable.")
