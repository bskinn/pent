.. Pattern-level semantics

Nomenclature and Definitions: Patterns
======================================

A ``pent`` *pattern* is a series of whitespace-delimited
:doc:`tokens <tokens>` that represents **all** non-whitespace
content on a given line of text.

A blank line---one that is empty, or contains only
whitespace---can be matched with an empty pattern string:

.. doctest:: blank

    >>> check_pattern(pattern="", text="")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="", text="          ")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="", text="     \t   ")
    MATCH
    <BLANKLINE>

If a line contains one piece of non-whitespace text,
a single token will suffice to match the whole line:

.. doctest:: one_piece

    >>> check_pattern(pattern="&.", text="foo")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&.", text="     foo")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#..i", text="-5")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#..i", text="    50000   ")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#..f", text="2")  # Wrong number type
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#.-i", text="2")  # Wrong number sign
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="", text="42")  # Line is not blank
    NO MATCH
    <BLANKLINE>

If a line contains more than one piece of non-whitespace text,
**all pieces** must be matched by a token in the pattern:

.. doctest:: multi_pieces

    >>> check_pattern(pattern="&+", text="foo bar baz")  # One-or-more gets all three
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&. &.", text="foo bar baz")  # Only 2/3 words matched
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&. #..i", text="foo 42")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&+ #..i", text="foo bar baz 42")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#+.i", text="-2 -1 0 1 2")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#+.i", text="-2 -1 foo 1 2")
    NO MATCH
    <BLANKLINE>

Be careful when using "|cour|\ ~\ |/cour|" and
"|\cour|\ &+\ |/cour|", as they **may** match
more aggressively than expected:

    >>> check_pattern(pattern="~ #+.i", text="foo bar 42 34")
    MATCH
    <BLANKLINE>
    >>> show_capture(pattern="~! #+.i", text="foo bar 42 34")
    [[['foo', 'bar']]]
    <BLANKLINE>
    >>> check_pattern(pattern="&+ #+.i", text="foo bar 42 34")
    MATCH
    <BLANKLINE>
    >>> show_capture(pattern="&!+ #+.i", text="foo bar 42 34")
    [[['foo', 'bar', '42']]]
    <BLANKLINE>
    >>> check_pattern(pattern="&+ #+.i", text="foo 42 bar 34")
    MATCH
    <BLANKLINE>
    >>> show_capture(pattern="&!+ #+.i", text="foo 42 bar 34")
    [[['foo', '42', 'bar']]]
    <BLANKLINE>


Punctuation will foul matches unless explicitly accounted for:

*Commas, periods, etc.*

*Pattern commentary, some simple examples, links to other tutorial example pages*


Optional Line Flag: |cour|\ ?\ |/cour|
--------------------------------------

*DISCUSS*
