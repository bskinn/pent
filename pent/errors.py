r"""*Custom exceptions for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    10 Sep 2018

**Copyright**
    \(c) Brian Skinn 2018-2019

**Source Repository**
    http://www.github.com/bskinn/pent

**Documentation**
    http://pent.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""


class PentError(Exception):  # pragma: no cover
    """Superclass for all custom pent errors."""

    pass


class TokenError(PentError):  # pragma: no cover
    """Raised during attempts to parse an invalid token."""

    def __init__(self, token):
        """Instantiate a ``TokenError``."""
        self.token = token

    def __str__(self):
        """Generate a more-informative error message."""
        return "'{}' is an invalid pent token".format(self.token)


class LineError(PentError):  # pragma: no cover
    """Raised during attempts to parse invalid token sequences."""

    def __init__(self, line):
        """Instantiate a ``LineError``."""
        self.line = line

    def __str__(self):
        """Generate a more-informative error message."""
        return "'{}' is an invalid pent token sequence".format(self.line)


class SectionError(PentError):  # pragma: no cover
    """Raised from failed attempts to parse a Parser section."""

    def __init__(self, msg=""):
        """Instantiate a ``SectionError``."""
        self.msg = msg

    def __str__(self):
        """Generate a more-informative error message."""
        return "Bad Parser section: {}".format(self.msg)


class ThruListError(PentError):  # pragma: no cover
    """Raised from failed ThruList indexing attempts."""

    def __init__(self, msg=""):
        """Instantiate a ``ThruListError``."""
        self.msg = msg

    def __str__(self):
        """Generate a more-informative error message."""
        return "Invalid ThruList index: {}".format(self.msg)
