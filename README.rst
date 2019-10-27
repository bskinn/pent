pent Extracts Numerical Text
============================

*Mini-language driven parser for structured numerical (or other) data
in free text*

**Current Development Version:**

.. image::  https://img.shields.io/travis/bskinn/pent?label=travis-ci&logo=travis
    :target: https://travis-ci.org/bskinn/pent

.. image:: https://codecov.io/gh/bskinn/pent/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/bskinn/pent

**Most Recent Stable Release:**

.. image:: https://img.shields.io/pypi/v/pent.svg?logo=pypi
    :target: https://pypi.org/project/pent

.. image:: https://img.shields.io/pypi/pyversions/pent.svg?logo=python

**Info:**

.. image:: https://img.shields.io/readthedocs/pent/latest
    :target: http://pent.readthedocs.io/en/latest/

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://github.com/bskinn/pent/blob/stable/LICENSE.txt

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

----

**Do you have structured numerical data stored as text?**

**Does the idea of writing regex to parse it fill you with loathing?**

``pent`` *can help!*

Say you have data in a text file that looks like this:

.. code::

    $vibrational_frequencies
    18
        0        0.000000
        1        0.000000
        2        0.000000
        3        0.000000
        4        0.000000
        5        0.000000
        6      194.490162
        7      198.587114
        8      389.931897
        9      402.713910
       10      538.244274
       11      542.017838
       12      548.246738
       13      800.613516
       14     1203.096114
       15     1342.200360
       16     1349.543713
       17     1885.157022

What's the most efficient way to get that list of floats
extracted into a ``numpy`` array?
There's clearly structure here, but how to exploit it?

It would work to import the text into a spreadsheet, split columns appropriately,
`re-export just the one column to CSV <https://github.com/bskinn/excel-csvexporter>`__,
and import to Python from there,
but that's just exhausting drudgery if there are dozens of files involved.

Automating the parsing via a line-by-line string search would work fine
(this is how |cclib|_ implements its data imports), but a new line-by-line
method is needed for every new kind of dataset,
and any time the formatting of a given dataset changes.

It's not *too* hard to
`write regex <https://github.com/bskinn/opan/blob/12c8e98de2a81bbd570c821644063d975e2ab03e/opan/hess.py#L688-L701>`__
that will parse it, but because of the mechanics of regex group captures
you have to write two patterns: one to capture the entire block, including the header
(to ensure other, similarly-formatted data isn't also captured); and then one to
`iterate line-by-line <https://github.com/bskinn/opan/blob/12c8e98de2a81bbd570c821644063d975e2ab03e/opan/hess.py#L1192-L1207>`__
over just the data block to extract the individual values. And, of course, one has to actually *write*
(and proofread, and maintain) the regex.

``pent`` **provides a better way.**

The data above comes from `this file <https://github.com/bskinn/pent/blob/cbb3c9b24c773b51b4988485b838537043ec8299/pent/test/C2F4_01.hess>`__,
``C2F4_01.hess``. With ``pent``, the data can be pulled into ``numpy`` in just a couple
of lines, without writing **any** regex at all:

.. code:: python

    >>> data = pathlib.Path("pent", "test", "C2F4_01.hess").read_text()
    >>> prs = pent.Parser(
    ...     head=("@.$vibrational_frequencies", "#.+i"),
    ...     body=("#.+i #!..f")
    ... )
    >>> arr = np.array(prs.capture_body(data), dtype=float)
    >>> print(arr)
    [[[   0.      ]
      [   0.      ]
      [   0.      ]
      [   0.      ]
      [   0.      ]
      [   0.      ]
      [ 194.490162]
      [ 198.587114]
      [ 389.931897]
      [ 402.71391 ]
      [ 538.244274]
      [ 542.017838]
      [ 548.246738]
      [ 800.613516]
      [1203.096114]
      [1342.20036 ]
      [1349.543713]
      [1885.157022]]]

The result comes out as a length-one list of 2-D matrices, since the search pattern
occurs only once in the data file. The single 2-D matrix is laid out as a
column vector, because the data runs down the column in the file.

``pent`` can handle larger, more deeply nested data as well.
Take `this 18x18 matrix <https://github.com/bskinn/pent/blob/cbb3c9b24c773b51b4988485b838537043ec8299/pent/test/C2F4_01.hess#L13-L71>`__
within ``C2F4_01.hess``, for example.
Here, it's necessary to pass a ``Parser`` as the *body* of another ``Parser``:

.. code:: python

    >>> prs_hess = pent.Parser(
    ...     head=("@.$hessian", "#.+i"),
    ...     body=pent.Parser(
    ...         head="#++i",
    ...         body="#.+i #!+.f"
    ...     )
    ... )
    >>> result = prs_hess.capture_body(data)
    >>> arr = np.column_stack([np.array(_, dtype=float) for _ in result[0]])
    >>> print(arr[:3, :7])
    [[ 0.468819 -0.006771  0.020586 -0.38269   0.017874 -0.05449  -0.044552]
     [-0.006719  0.022602 -0.016183  0.010997 -0.033397  0.014422 -0.01501 ]
     [ 0.020559 -0.016184  0.066859 -0.033601  0.014417 -0.072836  0.045825]]

The need for the generator expression, the ``[0]`` index into ``result``,
and the composition via ``np.column_stack`` arises
due to the manner in which ``pent`` returns data from a nested match like this.
See the `documentation <https://pent.readthedocs.io/en/latest>`__,
in particular `this example <https://pent.readthedocs.io/en/latest/tutorial/examples/nested_parsers.html>`__,
for more information.

The grammar of the ``pent`` mini-language is designed to be flexible enough that
it should handle essentially all well-formed structured data, and even some data
that's not especially well formed. Some datasets will require post-processing of the
data structures generated by ``pent`` before they can be pulled into
``numpy`` (see, e.g., `this test <https://github.com/bskinn/pent/blob/eaa79a09af88d3836deff4f4efaff26ea085786b/pent/test/pent_livedata.py#L329-L345>`__,
parsing `this data block <https://github.com/bskinn/pent/blob/eaa79a09af88d3836deff4f4efaff26ea085786b/pent/test/mwfn_li_di_elfbasin.txt#L520-L526>`__).

-----

Beta releases available on `PyPI <https://pypi.org/project/pent>`__: ``pip install pent``

Full documentation is hosted at
`Read The Docs <http://pent.readthedocs.io/en/latest/>`__.

Source on `GitHub <https://github.com/bskinn/pent>`__.  Bug reports,
feature requests, and ``Parser`` construction help requests
are welcomed at the
`Issues <https://github.com/bskinn/pent/issues>`__ page there.

Copyright (c) Brian Skinn 2018-2019

License: The MIT License. See `LICENSE.txt <https://github.com/bskinn/pent/blob/master/LICENSE.txt>`__
for full license terms.


.. |cclib| replace:: ``cclib``

.. _cclib: https://github.com/cclib/cclib
