r"""*Custom exceptions for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    10 Sep 2018

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


class PentError(Exception):  # pragma: no cover
    pass


class BadTokenError(PentError):  # pragma: no cover
    """Raised during attempts to parse an invalid token."""

    def __init__(self, token):
        self.token = token

    def __str__(self):
        return "'{}' is an invalid pent token".format(self.token)


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
