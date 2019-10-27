.. Misc token

The Misc Token
==============

Sometimes, data is laid out in text in a fashion
where it cannot be matched using only numerical values.
Either some elements of the data of interest are themselves
non-numeric, or there are non-numeric portions of content
interspersed with the numeric data of interest.
``pent`` provides the "misc" token
(|cour|\ &\ |/cour|) to handle these kinds of situations.

Take the following data, which is an example of the
`XYZ format <https://en.wikipedia.org/wiki/XYZ_file_format>`__
for representing the atomic
coordinates of a chemical system:

.. doctest:: misc

    >>> text_xyz = dedent("""
    ... 5
    ... Coordinates from MeCl2F_2
    ...   C      -3.081564      2.283942      0.044943
    ...   Cl     -1.303141      2.255173      0.064645
    ...   Cl     -3.706406      3.411601     -1.180577
    ...   F      -3.541771      2.647036      1.270358
    ...   H      -3.439068      1.277858     -0.199370
    ... """)

In this case, pretty much everything in the text block is of
interest. The first number indicates how many atoms are present
(useful for cross-checking the data import), the line of
text is an arbitrary string describing the chemical system,
and the data block provides the atomic symbol of each atom and
its xyz position in space.

.. _tutorial-examples-misc-splittingofany:

The following |Parser| will enable capture of the entire contents
of the string:

.. doctest:: misc

    >>> prs_xyz = pent.Parser(
    ...     head=("#!..i", "~!"),
    ...     body="&!. #!+.d",
    ... )

The atomic symbols and coordinates are most easily retrieved
with |capture_body|:

.. doctest:: misc

    >>> data_atoms = prs_xyz.capture_body(text_xyz)
    >>> data_atoms
    [[['C', '-3.081564', '2.283942', '0.044943'], ['Cl', '-1.303141', '2.255173', '0.064645'], ['Cl', '-3.706406', '3.411601', '-1.180577'], ['F', '-3.541771', '2.647036', '1.270358'], ['H', '-3.439068', '1.277858', '-0.199370']]]

The atom count and description can be retrieved with
|capture_struct|:

.. doctest:: misc

    >>> data_struct = prs_xyz.capture_struct(text_xyz)
    >>> data_struct[pent.ParserField.Head][0]
    ['5', 'Coordinates', 'from', 'MeCl2F_2']

Unlike in *body*, where two-dimensional structure is inferred in captured data,
in *head* and *tail* all captures are returned as elements of a single, flat |list|.

Currently, it is not possible to avoid the splitting of *all* captured content
at whitespace, even it it was captured from a single 'any' or 'literal' token.
:issue:`26` and/or :issue:`62` are planned and will provide mechanism(s)
to change this behavior.

-----

As an aside, in this particular case the 'misc' token was not strictly
necessary in the *body*, as the capturing 'any' token
(|cour|\ ~!\ |/cour|) would also have worked:

.. doctest:: misc

    >>> prs_any = pent.Parser(
    ...     head=("#.+i", "~"),
    ...     body="~! #!+.d",
    ... )
    >>> prs_any.capture_body(text_xyz)
    [[['C', '-3.081564', '2.283942', '0.044943'], ['Cl', '-1.303141', '2.255173', '0.064645'], ['Cl', '-3.706406', '3.411601', '-1.180577'], ['F', '-3.541771', '2.647036', '1.270358'], ['H', '-3.439068', '1.277858', '-0.199370']]]

However, there are situations where the ability
of the 'misc' token to match
only a single, arbitrary piece of whitespace-delimited
content is useful in order to narrow the specificity of
the |Parser| match.


Another example of the use of the 'misc' token is given
at :doc:`post_process`.

