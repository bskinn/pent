.. Demonstrating use-cases for required/optional/no space after

Required/Optional/Prohibited Trailing Whitespace
================================================

By default, number (|cour|\ #\ |/cour|),
misc (|cour|\ &\ |/cour|),
and literal (|cour|\ @\ |/cour|) tokens
require trailing whitespace to be present in the text
in order to match:

.. doctest:: space_after

    >>> text_space = dedent("""\
    ... foo: 5
    ... bar: 8
    ... """)
    >>> text_nospace = dedent("""\
    ... foo:5
    ... bar:8
    ... """)
    >>> prs_req = pent.Parser(body="&. #!.+i")
    >>> prs_req.capture_body(text_space)
    [[['5'], ['8']]]
    >>> prs_req.capture_body(text_nospace)
    []

``pent`` provides a means to make this trailing whitespace
either optional or prohibited, if needed.

Optional trailing whitespace is indicated with an
"|cour|\ o\ |/cour|" flag in the token:

.. doctest:: space_after

    >>> prs_opt = pent.Parser(body="&o. #!.+i")
    >>> prs_opt.capture_body(text_space)
    [[['5'], ['8']]]
    >>> prs_opt.capture_body(text_nospace)
    [[['5'], ['8']]]

Similarly, prohibited trailing whitespace is indicated with an
"|cour|\ x\ |/cour|" flag in the token:

.. doctest:: space_after

    >>> prs_prohib = pent.Parser(body="&x. #!.+i")
    >>> prs_prohib.capture_body(text_space)
    []
    >>> prs_prohib.capture_body(text_nospace)
    [[['5'], ['8']]]

If used in combination with the capturing "|cour|\ !\ |/cour|" flag,
the trailing-space flag is placed *before* the capturing flag;
e.g., as "|cour|\ &x!.\ |/cour|".

One common situation where this capability is needed
is when a number of interest is contained in prose text
and falls at the end of a sentence:

.. doctest:: space_after

    >>> text_prose = dedent("""\
    ... pi is approximately 3.14159.
    ... """)
    >>> pent.Parser(body="~ #!..f &.").capture_body(text_prose)
    []
    >>> pent.Parser(body="~ #x!..f &.").capture_body(text_prose)
    [[['3.14159']]]

Don't forget to include a token for that trailing period!
The |Parser| won't find a match, otherwise:

.. doctest:: space_after

    >>> pent.Parser(body="~ #x!..f").capture_body(text_prose)
    []


Limitations of the "Any" Token
------------------------------

Note that, as currently implemented, the 'any' token
(|cour|\ ~\ |/cour|) does not allow specification of
optional or prohibited trailing whitespace; any
content that it matches *must* be followed by
whitespace for the |Parser| to work:

.. doctest:: space_after

    >>> text_sandwich = dedent("""\
    ... This number3.14159is sandwiched in text.
    ... """)
    >>> pent.Parser(body="~ #x!..f ~").capture_body(text_sandwich)
    []

In order to match this value, the preceding text must be matched
either by a literal or a misc token:

.. doctest:: space_after

    >>> pent.Parser(body="~ @x.number #x!..f ~").capture_body(text_sandwich)
    [[['3.14159']]]
    >>> pent.Parser(body="~ &x. #x!..f ~").capture_body(text_sandwich)
    [[['3.14159']]]

This deficiency will be addressed in :issue:`78`.
