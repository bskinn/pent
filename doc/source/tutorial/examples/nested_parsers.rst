.. Capturing with nested Parsers

Capturing with Nested |Parser|\ s
=================================

``pent`` is also able to parse and capture higher-dimensional data
stored as free text. Take the following data string:

.. doctest:: orca_hess

    >>> text = dedent("""\
    ... $hessian
    ... 4
    ...                   0          1
    ...       0       0.473532   0.004379
    ...       1       0.004785   0.028807
    ...       2       0.004785  -0.022335
    ...       3      -0.418007   0.008333
    ...                   2          3
    ...       0       0.004379  -0.416666
    ...       1      -0.022335   0.008067
    ...       2       0.028807   0.008067
    ...       3       0.008333   0.420926
    ... """)

`text` represents a 4x4 matrix, with the first two columns printed in one section,
and the second two columns printed in a separate, following section.
Each row and column is marked with its respective index.
In order to import this data successfully, the *body* of the main
|Parser| will have to be set to a different, inner |Parser|.


Defining the Inner |Parser|
---------------------------

Each section of data columns starts with a row containing only positive integers,
which does not need to be captured. After that leading row are
multiple rows with data, each of which leads with a single
positive integer, followed by decimal-format data of any sign:

.. doctest:: orca_hess

    >>> text_inner = dedent("""\
    ...                   0          1
    ...       0       0.473532   0.004379
    ...       1       0.004785   0.028807
    ...       2       0.004785  -0.022335
    ...       3      -0.418007   0.008333
    ... """)

One way to construct a |Parser| for this internal block is as follows:

.. doctest:: orca_hess

    >>> prs_inner = pent.Parser(
    ...     head="#++i",
    ...     body="#.+i #!+.d",
    ... )
    >>> prs_inner.capture_body(text_inner)
    [[['0.473532', '0.004379'], ['0.004785', '0.028807'], ['0.004785', '-0.022335'], ['-0.418007', '0.008333']]]


Defining the Outer |Parser|
---------------------------

The outer |Parser| then makes use of the inner |Parser| as its *body*,
with the two header lines defined in *head*:

.. doctest:: orca_hess

    >>> prs_outer = pent.Parser(
    ...     head=("@.$hessian", "#.+i"),
    ...     body=prs_inner,
    ... )
    >>> data = prs_outer.capture_body(text)
    >>> data
    [[[['0.473532', '0.004379'], ['0.004785', '0.028807'], ['0.004785', '-0.022335'], ['-0.418007', '0.008333']], [['0.004379', '-0.416666'], ['-0.022335', '0.008067'], ['0.028807', '0.008067'], ['0.008333', '0.420926']]]]


Structure of the Returned *data*
--------------------------------

The structure of the list returned by |capture_body| nests four levels deep:

.. doctest:: orca_hess

    >>> arr = np.asarray(data, dtype=float)
    >>> arr.shape
    (1, 2, 4, 2)


This is because:

1. Each block of data is returned as a matrix (adds two levels);

2. The *body* of *prs_outer* is a |Parser| (adds one level); and

3. The |capture_body| method wraps everything in a list (adds one level).

So, working from left to right, the |cour|\ (1, 2, 4, 2)\ |/cour|
shape of the data arises because:

1. The overall *prs_outer* matched **1 time**;

2. The inner *prs_inner*, as the *body* of *prs_outer*, matched **2 times**; and

3. Both blocks of data matched by *prs_inner* have **4 rows** and **2 columns**


Reassembling the Full 4x4 Matrix
--------------------------------

In cases like this, ``numpy``'s :func:`~numpy.column_stack` provides
a simple way to reassemble the full 4x4 matrix of data, though
it is necessary to convert each matrix to an |ndarray| separately:

.. doctest:: orca_hess

    >>> np.column_stack([np.asarray(block, dtype=float) for block in data[0]])
    array([[ 0.473532,  0.004379,  0.004379, -0.416666],
           [ 0.004785,  0.028807, -0.022335,  0.008067],
           [ 0.004785, -0.022335,  0.028807,  0.008067],
           [-0.418007,  0.008333,  0.008333,  0.420926]])

`data[0]` is used instead of `data` in the generator expression
so that the two inner 4x2 blocks of data are yielded separately to :func:`~numpy.asarray`.

Coping with Mismatched Data Block Sizes
---------------------------------------

Nothing guarantees that the data in a chunk of text will have properly matched
internal dimensions, however. ``pent`` will still import the data, but
it may not be possible to pull it directly into a ``numpy`` array
as was done above:

.. doctest:: orca_hess

    >>> text2 = dedent("""\
    ... $hessian
    ... 4
    ...                   0          1
    ...       0       0.473532   0.004379
    ...       1       0.004785   0.028807
    ...       2       0.004785  -0.022335
    ...       3      -0.418007   0.008333
    ...                   2          3
    ...       0       0.004379  -0.416666
    ...       1      -0.022335   0.008067
    ... """)
    >>> data2 = prs_outer.capture_body(text2)
    >>> data2
    [[[['0.473532', '0.004379'], ['0.004785', '0.028807'], ['0.004785', '-0.022335'], ['-0.418007', '0.008333']], [['0.004379', '-0.416666'], ['-0.022335', '0.008067']]]]
    >>> np.asarray(data2, dtype=float)
    Traceback (most recent call last):
    ...
    ValueError: setting an array element with a sequence.
    >>> np.column_stack([np.asarray(block, dtype=float) for block in data2[0]])
    Traceback (most recent call last):
    ...
    ValueError: all the input array dimensions except for the concatenation axis must match exactly

In situations like this, the returned data structure either must be processed
with methods that can accommodate the missing data, or the missing data must be explicitly
filled in before conversion to |ndarray|.
