.. Token-level semantics

Basic Usage: Tokens
===================

``pent`` understands four kinds of tokens, which match varying types of content.
One is an :ref:`'any' token <tutorial-basics-tokens-anytoken>`,
which matches an arbitrary span of whitespace and/or
non-whitespace content. The other three types are intended to match specific kinds of
content within the line of text that are often, but not always,
separated from surrounding content by whitespace.

All four kinds of tokens accept a :ref:`flag <tutorial-basics-tokens-captureflag>`
that instructs the encapsulating
|Parser| to capture the content matching the token for output.
A subset of the tokens accepts a :ref:`flag <tutorial-basics-tokens-spaceflags>`
that alters how the |Parser| handles the presence or absence of whitespace
following the content matching the token.


.. _tutorial-basics-tokens-anytoken:

'Any'
-----

The 'any' token:

|cour|\ ~\ |/cour|

...will match **anything**, including a completely blank line.
It behaves essentially the same as "|cour|\ .*\ |/cour|" in regex.

Currently, the 'any' token only accepts the
:ref:`'capture' flag <tutorial-basics-tokens-captureflag>`
(becoming "|cour|\ ~!\ |/cour|"). Addition of support for the
:ref:`'space-after' flags <tutorial-basics-tokens-spaceflags>`
is planned (:issue:`78`).

Note that any content matched by a capturing 'any' token will be
split at whitespace in |Parser| output.


.. _tutorial-basics-tokens-misctoken:

'Misc'
------

The 'misc' token:

|cour|\ &\ |/cour|

...matches any sequence of non-whitespace characters.
Its uses are similar to the :ref:`'any' token <tutorial-basics-tokens-anytoken>`,
except that its match
is confined to a single whitespace-delimited piece of content.
It is mainly intended for use on non-numerical data
whose content is not constant, and thus
the :ref:`'literal' token <tutorial-basics-tokens-literaltoken>` cannot be used.

The 'misc' token has one required argument, indicating whether
it should match exactly one piece of content
(|cour|\ &.\ |/cour|) or one-or-more pieces of content
(|cour|\ &+\ |/cour|). When matching one-or-more,
the 'misc' token interleaves *required* whitespace
between each reptition.

At this time, the functional difference between
"|cour|\ ~\ |/cour|" and "|cour|\ &+\ |/cour|" is minimal.

The 'misc' token accepts both the
:ref:`capture flag <tutorial-basics-tokens-captureflag>`
and the :ref:`space-after <tutorial-basics-tokens-spaceflags>` modifier flags.


.. _tutorial-basics-tokens-literaltoken:

'Literal'
---------

The 'literal' token:

|cour|\ @\ |/cour|

...matches an *exact* sequence of one or more
whitespace-delimited characters, which is provided as a required argument
in the token definition.

Similar to the :ref:`'misc' token <tutorial-basics-tokens-misctoken>`,
the 'literal' token also has
the quantity specifier as a required argument:
either "|cour|\ @.\ |/cour|" for exactly one match
or "|cour|\ @+\ |/cour|" for one-or-more matches.

The argument for the string to be matched follows the
quantity argument. Thus, to match the text
|cour|\ foo\ |/cour| exactly once a suitable token
might be "|cour|\ @.foo\ |/cour|".

In the situation where it's needed to match a literal string
containing a space, the entire token can be enclosed in
quotes: "|cour|\ '@.this has spaces'\ |/cour|".

The 'literal' token differs from the
:ref:`'misc' <tutorial-basics-tokens-misctoken>` and
:ref:`'number' <tutorial-basics-tokens-numbertoken>` tokens
in that when the one-or-more argument is used, it **prohibits**
whitespace between the repetitions.
This allows, e.g., a long sequence of hyphens to be represented
by a token like "|cour|\ @+-\ |/cour|". Similarly, a long
sequence of alternating hyphens and spaces could be represented
by "|cour|\ '@+- '\ |/cour|".

The 'literal' token accepts both the
:ref:`capture flag <tutorial-basics-tokens-captureflag>`
and the :ref:`space-after <tutorial-basics-tokens-spaceflags>` modifier flags.


.. _tutorial-basics-tokens-numbertoken:

'Number'
--------

The 'number' token:

|cour|\ #\ |/cour|

...allows for selectively matching numbers of varying
types in the text being parsed; in particular, matches can be constrained 
by sign (positive, negative, or either) or by format
(integer, decimal, or scientific notation; or, combinations of these).

The 'number' token takes three required, single-character arguments:

1. Quantity: |br|
   |cour|\ #.\ |/cour| for exactly one, or |br|
   |cour|\ #+\ |/cour| for one-or-more. |br|
   |nbsp|

2. Sign: |br|
   |cour|\ #[.+]+\ |/cour| for positive, |br|
   |cour|\ #[.+]-\ |/cour| for negative, or |br|
   |cour|\ #[.+].\ |/cour| for either sign. |br|
   |nbsp|

3. Number Format: |br| 
   |cour|\ #[.+][.-+]i\ |/cour| for integer, |br|
   |cour|\ #[.+][.-+]d\ |/cour| for decimal, |br|
   |cour|\ #[.+][.-+]s\ |/cour| for scientific notation, |br|
   |cour|\ #[.+][.-+]f\ |/cour| for float (decimal or scientific notation) |br|
   |cour|\ #[.+][.-+]g\ |/cour| for general (integer or float).

The ability to specify different types of number formatting was implemented
for this token because it is often the case that numbers printed
in different formats have different semantic significance,
and it's thus useful to be able to filter/capture based on that format.
:ref:`This example <tutorial-examples-singleparser-multiplevalues>`
illustrates a simplified case of this.

As with the :ref:`'misc' token <tutorial-basics-tokens-misctoken>`,
when matching in one-or-more quantity mode,
the 'number' token interleaves *required* whitespace between each reptition.

The 'number' token accepts both the
:ref:`capture flag <tutorial-basics-tokens-captureflag>`
and the :ref:`space-after <tutorial-basics-tokens-spaceflags>` modifier flags.


.. _tutorial=defs-tokens-flags:

Token Flags
-----------

Currently, two types of flags can be passed to tokens:
:ref:`capture flag <tutorial-basics-tokens-captureflag>`
and the :ref:`space-after <tutorial-basics-tokens-spaceflags>` modifier flags.

If both flags are used in a given token, the space-after modifier
flag must **precede** the capture flag.


.. _tutorial-basics-tokens-captureflag:

Capture Flag
~~~~~~~~~~~~

|cour|\ !\ |/cour|

In most cases, not all of the data in a block of text is of interest
for downstream processing. Thus, ``pent`` provides the token-level
'capture' flag, "|cour|\ !\ |/cour|", which marks
the content of that token for inclusion in the output of
:meth:`~pent.parser.Parser.capture_body` and
:meth:`~pent.parser.Parser.capture_struct`.
The 'capture' flag is an integral part of all of the
:doc:`tutorial examples </tutorial/examples>`.


.. _tutorial-basics-tokens-spaceflags:

Space-After Flags
~~~~~~~~~~~~~~~~~

|cour|\ o\ |/cour|

...and:

|cour|\ x\ |/cour|

With no space-after flag provided, all tokens *REQUIRE* the presence
of trailing whitespace (or EOL)
in order to match. This is because most content is anticipated to be
whitespace-delineated, and thus this default leads to
more concise |Parser| definitions.

However, there are situations where changing this behavior is
useful for defining a well-targeted |Parser|, and some where
changing it is necessary in order to compose
a functional |Parser| at all.

As an example, take the following line of text:

.. code::

    The foo is in the foo.

The token "|cour|\ @.foo\ |/cour|"
would match the first occurrence of the word "foo",
because it has whitespace after it, but it would
*not* match the second occurrence, since it is
immediately followed by a period.

In order to match both occurrences, the
'optional trailing whitespace flag',
"|cour|\ o\ |/cour|", could be added, leading
to the token "|cour|\ @o.foo\ |/cour|".

If it were desired only to match the second occurrence,
the 'prohibited trailing whitespace flag',
"|cour|\ x\ |/cour|", could be added,
yielding "|cour|\ @x.foo\ |/cour|".

:doc:`This tutorial example </tutorial/examples/space_after>`
provides further illustration of the use of these flags
in more-realistic situations.

