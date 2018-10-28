r"""*Custom list object for* ``pent``.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    3 Oct 2018

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

from .errors import ThruListError


class ThruList(list):
    """List that passes through `key` if len == 1."""

    def __getitem__(self, key):
        """Return list item, or element of first item if len == 1."""
        if isinstance(key, int):
            return super().__getitem__(key)

        else:
            if len(self) == 1:
                return self[0][key]
            elif len(self) == 0:
                raise ThruListError(
                    msg="Cannot pass through key when len == 0"
                )
            else:
                raise ThruListError(msg="Numeric index required for len != 1")


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
