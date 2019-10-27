.. Pattern-level semantics

Basic Usage: Patterns
=====================

A ``pent`` *pattern* is a series of :doc:`tokens <tokens>` that
represents **all** non-whitespace content on a given line of text.
The tokens (and their arguments) are delimited by whitespace.

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
    >>> check_pattern(pattern="#+.i", text="-2 -1 foo 1 2")  # 'foo' is not an int
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#+.i &. #+.i", text="-2 -1 foo 1 2")
    MATCH
    <BLANKLINE>

Be careful when using "|cour|\ ~\ |/cour|" and
"|\cour|\ &+\ |/cour|", as they **may** match
more aggressively than expected:

.. doctest:: aggressive_matching

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

.. doctest:: punctuation

    >>> check_pattern(pattern="#+.i", text="1 2 ---- 3 4")
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="#+.i &. #+.i", text="1 2 ---- 3 4")
    MATCH
    <BLANKLINE>


In situations where punctuation is directly adjacent to the content
to be captured, the :ref:`space-after flags <tutorial-basics-tokens-spaceflags>`
must be used to modify ``pent``'s expectations for whitespace:

.. doctest:: whitespace

    >>> check_pattern(pattern="~ #..d @..", text="The value is 3.1415.")  # No space between number and '.'
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="~ #x..d @..", text="The value is 3.1415.")
    MATCH
    <BLANKLINE>


In situations where some initial content will definitely appear on a line,
but some additional trailing content *may or may not* appear at the end of the line,
it's important to use one of the space-after modifier flags in order for
``pent`` to find a match when the trailing content is absent.
This is because the default required
trailing whitespace will (naturally) *require* whitespace to be present
between the end of the matched content and the end of the line,
and if EOL immediately follows the content the pattern match will fail,
since the required whitespace is absent:

.. doctest:: eol_optional

    >>> check_pattern(pattern="&. #.+i ~", text="always 42 sometimes")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&. #.+i ~", text="always 42")
    NO MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&. #.+i ~", text="always 42   ")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&. #x.+i ~", text="always 42")
    MATCH
    <BLANKLINE>
    >>> check_pattern(pattern="&. #x.+i ~", text="always 42 sometimes")
    MATCH
    <BLANKLINE>


.. _tutorial-basics-patterns-optionallineflag:

Optional Line Flag: |cour|\ ?\ |/cour|
--------------------------------------

In some cases, an entire line of text will be present in some occurrences
of a desired |Parser| match with a block of text, but absent in others.
To accommodate such situations, ``pent`` recognizes an 'optional-line flag' in a pattern.
This flag is a sole "|cour|\ ?\ |/cour|", occurring as the first "token"
in the pattern. Inclusion of this flag will cause the pattern
to match in the following three cases:

1. A line is present that completely matches the optional pattern
   (per usual behavior).

2. A blank line (no non-whitespace content) is present where the
   optional pattern would match.

3. **NO** line is present where the optional pattern would match.

It is difficult to construct meaningful examples of this behavior
without using a full |Parser| construction; as such, see
:ref:`this tutorial page <tutorial-examples-optline-threetypes>`
for more details.

