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


class ThruList(list):
    """List that passes through `key` if len == 1."""

    def __getitem__(self, key):
        """Return list item, or element of BLAH."""
        if not isinstance(key, int) and len(self) == 1:
            return self[0][key]
        else:
            try:
                return super().__getitem__(key)
            except TypeError:
                raise IndexError("Key '{}' not found on item 0".format(key))


if __name__ == "__main__":  # pragma: no cover
    print("Module not executable.")
