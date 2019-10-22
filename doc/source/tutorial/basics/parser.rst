.. Introducing the Parser semantics

Basic Usage: |Parsers|
======================

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
:doc:`examples section </tutorial/examples>` of the tutorial.


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




----

|br|

----

**Drafting Notes**


*ordered iterables of pattern strings maps to
sequential lines*

for *body*, means that the sequence of lines
will be found multiple times in 'collated' fashion
(need example here, or in examples)
