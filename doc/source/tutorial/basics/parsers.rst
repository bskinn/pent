.. Introducing the Parser semantics

Basic Usage: Parsers
====================

The |Parser| is the main user-facing interface to ``pent``,
where the patterns matching the data of interest
are defined. |Parsers| are created with three arguments,
*head*, *body*, and *tail*. All |Parsers| must have a *body*;
*head* and *tail* are optional.

A section of text matched by
a given |Parser| will have the following structure:

- If *head* is defined, it will be matched exactly once,
  and its content must immediately precede the *body* content.

- *body* will be matched one or more times.

- If *tail* is defined, it will be matched exactly once,
  and its content must immediately follow the *body* content.

Each of *head*, *body*, and *tail* can be one of three things:

1. A single ``pent`` :doc:`pattern <patterns>`,
   matching a single line of text

2. An ordered iterable (|tuple|, |list|, etc.) of patterns,
   matching a number of lines of text equal to the length
   of the iterable

3. A |Parser|, matching its entire contents

The syntax and matching structure of |Parsers| using
these three kinds of arguments are illustrated below
using trivial examples. Application of ``pent`` to
more-realistic situations is demonstrated in the
:doc:`Examples section </tutorial/examples>` of the tutorial.

In the below examples, most illustrations are of the use
of *head*, rather than *tail*. However, the principles
apply equally well to both.


Matching with Single Patterns
-----------------------------

The simplest possible |Parser| only has *body* defined,
containing a single ``pent``
:doc:`pattern <patterns>`:

.. doctest:: single_patterns

    >>> prs = pent.Parser(body="@!.bar")
    >>> text = """foo
    ...           bar
    ...           baz"""
    >>> prs.capture_body(text)
    [[['bar']]]

As noted, *body* will match multiple times in a row:

.. doctest:: single_patterns

    >>> text = """foo
    ...           bar
    ...           bar
    ...           bar
    ...           baz"""
    >>> prs.capture_body(text)
    [[['bar'], ['bar'], ['bar']]]

Multiple occurrences of *body* in the text will match independently:

.. doctest:: single_patterns

    >>> text = """foo
    ...           bar
    ...           baz
    ...           bar
    ...           baz"""
    >>> prs.capture_body(text)
    [[['bar']], [['bar']]]

If only that first |cour|\ bar\ |/cour| is of interest,
the |Parser| match can be constrained with a *head*:

.. doctest:: single_patterns

    >>> prs_head = pent.Parser(head="@.foo", body="@!.bar")
    >>> prs_head.capture_body(text)
    [[['bar']]]

Adding just a *tail* doesn't really help, since
|cour|\ baz\ |/cour| follows both instances of
|cour|\ bar\ |/cour|:

.. doctest:: single_patterns

    >>> prs_tail = pent.Parser(body="@!.bar", tail="@.baz")
    >>> prs_tail.capture_body(text)
    [[['bar']], [['bar']]]


Matching with Iterables of Patterns
-----------------------------------

Sometimes data is structured in such a way that
it's necessary to associate more than one line of text
with a given portion of a |Parser|. This is most
common with *head* and *tail*, but it can occur with
*body* as well. These situations are addressed
by using iterables of patterns when
instantiating a |Parser|.

The following is a situation where the header
portion of the data contains two lines, 
one being a string label and the other being a series
of integers, and it's
important to capture only the "wanted" data block:

.. doctest:: iterables

    >>> text = """WANTED_DATA
    ...           1    2     3
    ...           1.5  2.1   1.1
    ...           
    ...           UNWANTED_DATA
    ...           1    2     3
    ...           0.1  0.4   0.2
    ...           """
    >>> pent.Parser(
    ...     head=("@.WANTED_DATA", "#++i"),
    ...     body="#!++d"
    ... ).capture_body(text)
    [[['1.5', '2.1', '1.1']]]

Note that even though |cour|\ WANTED_DATA\ |/cour| appears in the header
line of the 'unwanted' data block, since the
|cour|\ @.WANTED_DATA\ |/cour| token does not match
the *complete* contents of |cour|\ UNWANTED_DATA\ |/cour|,
the |Parser| does not match that second block.

If *head* were left out, or defined just to match the
rows of integers, both datasets would be retrieved:

.. doctest:: iterables

    >>> pent.Parser(head="#++i", body="#!++d").capture_body(text)
    [[['1.5', '2.1', '1.1']], [['0.1', '0.4', '0.2']]]

Situations calling for passing an iterable into *body* are less common,
but can occur if there is a strictly repeating, cyclic pattern to the
text to be parsed:

.. doctest:: iterables

    >>> text_good = """DATA
    ...                foo
    ...                bar
    ...                foo
    ...                bar
    ...                foo
    ...                bar"""
    >>> prs = pent.Parser(
    ...     head="@.DATA",
    ...     body=("@!.foo", "@!.bar")
    ... )
    >>> prs.capture_body(text_good)
    [[['foo', 'bar'], ['foo', 'bar'], ['foo', 'bar']]]

Note in the |cour|\ .capture_body()\ |/cour| output that even though
each |cour|\ foo\ |/cour| and |cour|\ bar\ |/cour| appear on separate
lines in the text, because the capture of each pair is defined
as the *body* of a single |Parser|, they end up being treated as though
they had been on the same line. Another example of this behavior
can be found in :doc:`this tutorial example </tutorial/examples/optional_line>`.

If the lines of body text are not strictly cyclic-repeating,
this approach won't work:

.. doctest:: iterables

    >>> text_bad = """DATA
    ...               foo
    ...               bar
    ...               
    ...               foo
    ...               bar"""
    >>> prs.capture_body(text_bad)
    [[['foo', 'bar']]]

There are other approaches that can handle such situations,
such as the
:ref:`optional-line pattern flag <tutorial-basics-patterns-optionallineflag>`:

.. doctest:: iterables

    >>> pent.Parser(
    ...     head="? @.DATA",
    ...     body=("@!.foo", "@!.bar")
    ... ).capture_body(text_bad)
    [[['foo', 'bar']], [['foo', 'bar']]]


Matching with a Nested |Parser|
-------------------------------

For data with more complex internal structure, often the best
way to match it is to pass a |Parser| to one or more of
*head*, *body*, or *tail*.

In situations where the header or footer content has a variable
number of lines that all match the same pattern, passing
a |Parser| is often the most concise approach, as it
exploits the implicit matching of one-or-more lines by
the *body* of that internal |Parser|:

.. doctest:: parsers

    >>> text_head = """foo
    ...                1 2 3
    ...                bar
    ...                bar
    ...
    ...                foo
    ...                1 2 3
    ...                4 5 6 7 8
    ...                9 10
    ...                bar
    ...                bar
    ...                bar"""
    >>> prs_head = pent.Parser(
    ...     head=pent.Parser(
    ...         head="@.foo",
    ...         body="#++i",
    ...     ),
    ...     body="@!.bar",
    ... )
    >>> prs_head.capture_body(text_head)
    [[['bar'], ['bar']], [['bar'], ['bar'], ['bar']]]

Another common use of an internal |Parser| is when
the main data content itself has a header/body/footer structure,
but it is also necessary to specify an overall header for the
data in order to avoid capturing multiple times within the
broader text:

.. doctest:: parsers

    >>> text_body = """WANTED
    ...                foo
    ...                bar
    ...                bar
    ...
    ...                UNWANTED
    ...                foo
    ...                bar
    ...                bar
    ...                bar
    ...                bar"""
    >>> prs_body = pent.Parser(
    ...     head="@.WANTED",
    ...     body=pent.Parser(
    ...         head="@.foo",
    ...         body="@!.bar",
    ...     ),
    ... )
    >>> prs_body.capture_body(text_body)
    [[[['bar'], ['bar']]]]

A clearer description of this approach is provided in
:doc:`this tutorial example </tutorial/examples/nested_parsers>`.
