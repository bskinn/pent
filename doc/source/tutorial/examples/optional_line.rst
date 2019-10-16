.. Demonstration of the optional-line token

The Optional-Line Token
=======================

In some situations, data is output in a fashion such
that a line of, e.g., header text is present in
some cases but not others. Take the following
fictitious example:

.. doctest:: optional_line

    >>> text = dedent("""
    ...     $DATA
    ...     ITERATION 1
    ...       0     1     2
    ...       1.5   3.1   2.4
    ...       3     4     5
    ...       -0.1  2.7   -9.3
    ...     ITERATION 2
    ...       0     1     2
    ...       1.6   2.9   1.8
    ...       3     4     5
    ...       -0.4  2.1   -8.7
    ... """)

This data block could be matched with triply nested |Parsers|:

.. doctest:: optional_line

    >>> prs_3x = pent.Parser(
    ...     head="@.$DATA",
    ...     body=pent.Parser(
    ...         head="@.ITERATION #..i",
    ...         body=pent.Parser(
    ...             head="#++i",
    ...             body="#!+.d",
    ...         ),
    ...     ),
    ... )
    >>> prs_3x.capture_body(text)
    [[[[['1.5', '3.1', '2.4']], [['-0.1', '2.7', '-9.3']]], [[['1.6', '2.9', '1.8']], [['-0.4', '2.1', '-8.7']]]]]

However, that definition is quite bulky, and for more complex
patterns and larger text inputs the three layers of nesting
can sometimes lead to problematically slow parsing times.

The :ref:`optional-line <tutorial-basics-patterns-optionallineflag>`
pattern flag allows for a simpler |Parser| structure here:

.. doctest:: optional_line

    >>> prs_opt = pent.Parser(
    ...     head=("? @.$DATA", "@.ITERATION #..i"),
    ...     body=pent.Parser(
    ...         head="#++i",
    ...         body="#!+.d",
    ...     ),
    ... )
    >>> prs_opt.capture_body(text)
    [[[['1.5', '3.1', '2.4']], [['-0.1', '2.7', '-9.3']]], [[['1.6', '2.9', '1.8']], [['-0.4', '2.1', '-8.7']]]]

The |cour|\ $DATA\ |/cour| is now wrapped into the *head*
of the outer of just *two* |Parsers|, flagged as optional so that
the |cour|\ ITERATION 2\ |/cour| can be matched.
This approach also returns the data with one fewer level of
|list| enclosure, which may be convenient in
downstream processing.

Since in this example the lines containing integers and the
lines containing decimals are *strictly* alternating,
yet another alternative would be to include the integer 'header'
lines as a non-captured portion of the *body*:

.. doctest:: optional_line

    >>> prs_opt = pent.Parser(
    ...     head=("? @.$DATA", "@.ITERATION #..i"),
    ...     body=pent.Parser(
    ...         body=("#++i", "#!+.d"),
    ...     )
    ... )
    >>> prs_opt.capture_body(text)
    [[[['1.5', '3.1', '2.4'], ['-0.1', '2.7', '-9.3']]], [[['1.6', '2.9', '1.8'], ['-0.4', '2.1', '-8.7']]]]

Doing it this way results in each |cour|\ ITERATION\ |/cour|\ 's
data being grouped into a two-dimensional matrix, instead of
each individual line of decimal values occurring in its own
matrix. This may or may not be desirable, depending on the
semantics of the data being captured.



*Examples of exactly how it matches*
------------------------------------