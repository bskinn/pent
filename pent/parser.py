r"""*Mini-language parser for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    8 Sep 2018

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

import attr

from .enums import Number, Sign
from .patterns import number_patterns, wordify_pattern, std_wordify


@attr.s
class Parser:
    """Mini-language parser for structured numerical data."""

    def convert_line(self, line):
        """Implement dirt-oversimple line converter."""
        import shlex

        tokens = shlex.split(line)

        pattern = r"(^|(?<=\n))"

        for t in tokens:
            if t == "*":
                pattern += ".*?"
            # ~ elif t.startswith('"') and t.endswith('"'):
            # ~ pattern += t[1:-1]
            elif t == "i":
                pattern += std_wordify(
                    number_patterns[(Number.Integer, Sign.Positive)]
                )
            elif t.startswith("!"):
                for c in t[1:]:
                    if c in "[\^$.|?*+(){}":
                        pattern += "\\" + c
                    else:
                        pattern += c
            else:
                raise ValueError("BAD PATTERN, NEED CUSTOM ERRORS!")

        # Plus anything to the end of the line
        # THIS APPROACH *MAY* END UP BEING PROBLEMATIC
        pattern += r".*?($|(?=\n))"

        return pattern
