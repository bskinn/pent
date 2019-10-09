.. Token-level semantics

Nomenclature and Definitions: Tokens
====================================

``pent`` understands four kinds of tokens, which match varying types of content.
One is an :ref:`'any' token <tutorial-defs-tokens-anytoken>`,
which matches an arbitrary span of whitespace and/or
non-whitespace content. The other three types are intended to match specific kinds of
content within the line of text that are often, but not always,
separated from surrounding content by whitespace.

All four kinds of tokens accept a :ref:`flag <tutorial-defs-tokens-captureflag>`
that instructs the encapsulating
|Parser| to capture the content matching the token for output.
A subset of the tokens accepts a :ref:`flag <tutorial-defs-tokens-spaceflags>`
that alters how the |Parser| handles the presence or absence of whitespace
following the content matching the token.


.. _tutorial-defs-tokens-anytoken:

The 'Any' Token: |cour|\ ~\ |/cour|
-----------------------------------

The 'any' token will match **anything**, including a completely blank line.
It behaves essentially the same as "|cour|\ .*\ |/cour|" in regex.

Currently, the 'any' token only accepts the
:ref:`'capture' flag <tutorial-defs-tokens-captureflag>`
(becoming "|cour|\ ~!\ |/cour|"). Addition of support for the
:ref:`'space-after' flags <tutorial-defs-tokens-spaceflags>`
is planned (:issue:`78`).

Note that any content matched by a capturing 'any' token will be
split at whitespace in |Parser| output.


.. _tutorial-defs-tokens-misctoken:

The 'Misc' Token: |cour|\ &\ |/cour|
------------------------------------

The 'misc' token matches any sequence of non-whitespace characters.
Its uses are similar to the :ref:`'any' token <tutorial-defs-tokens-anytoken>`,
except that its match
is confined to a single whitespace-delimited piece of content.
It is mainly intended for use on non-numerical data
whose content is not constant, and thus
the :ref:`'literal' token <tutorial-defs-tokens-literaltoken>` cannot be used.

The 'misc' token has one required argument, indicating whether
it should match exactly one piece of content
(|cour|\ &.\ |/cour|) or one-or-more pieces of content
(|cour|\ &+\ |/cour|). When matching one-or-more,
the 'misc' token interleaves *required* whitespace
between each reptition.

At this time, the functional difference between
"|cour|\ ~\ |/cour|" and "|cour|\ &+\ |/cour|" is minimal.

The 'misc' token accepts both the
:ref:`capture flag <tutorial-defs-tokens-captureflag>`
and the :ref:`space-after <tutorial-defs-tokens-spaceflags>` modifier flags.


.. _tutorial-defs-tokens-literaltoken:

The 'Literal' Token: |cour|\ @\ |/cour|
---------------------------------------

The 'literal' token matches an *exact* sequence of one or more
whitespace-delimited characters, which is provided as a required argument
in the token definition.

Similar to the :ref:`'misc' token <tutorial-defs-tokens-misctoken>`,
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
:ref:`'misc' <tutorial-defs-tokens-misctoken>` and
:ref:`'number' <tutorial-defs-tokens-numbertoken>` tokens
in that when the one-or-more argument is used, it **prohibits**
whitespace between the repetitions.
This allows, e.g., a long sequence of hyphens to be represented
by a token like "|cour|\ @+-\ |/cour|". Similarly, a long
sequence of alternating hyphens and spaces could be represented
by "|cour|\ '@+- '\ |/cour|".

The 'literal' token accepts both the
:ref:`capture flag <tutorial-defs-tokens-captureflag>`
and the :ref:`space-after <tutorial-defs-tokens-spaceflags>` modifier flags.


.. _tutorial-defs-tokens-numbertoken:

The 'Number' Token: |cour|\ #\ |/cour|
--------------------------------------

The 'number' token allows for selectively matching numbers of varying
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
   |cour|\ #[.+][.-+]f\ |/cour| for float (decimal or scinot) |br|
   |cour|\ #[.+][.-+]g\ |/cour| for general (integer or float).

The ability to specify different types of number formatting was implemented
for this token because it is often the case that numbers printed
in different formats have different semantic significance,
and it's thus useful to be able to filter/capture based on that format.
:ref:`This example <tutorial-examples-singleparser-multiplevalues>`
illustrates a simplified case of this.

As with the :ref:`'misc' token <tutorial-defs-tokens-misctoken>`,
when matching in one-or-more quantity mode,
the 'number' token interleaves *required* whitespace between each reptition.

The 'number' token accepts both the
:ref:`capture flag <tutorial-defs-tokens-captureflag>`
and the :ref:`space-after <tutorial-defs-tokens-spaceflags>` modifier flags.


Token Flags
-----------

.. _tutorial-defs-tokens-captureflag:

Capture Flag: |cour|\ !\ |/cour|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In most cases, not all of the data in a block of text is of interest
for downstream processing. Thus, ``pent`` provides the token-level
'capture' flag, "|cour|\ !\ |/cour|", which enables marking
of the specific content that should be included in the results of
:meth:`~pent.parser.Parser.capture_body` and
:meth:`~pent.parser.Parser.capture_struct`.
The 'capture' flag is an integral part of all of the
:doc:`tutorial examples </tutorial/examples>`.


.. _tutorial-defs-tokens-spaceflags:

Space-After Flags: |cour|\ o\ |/cour| and |cour|\ x\ |/cour|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, all tokens *REQUIRE* the presence of trailing whitespace (or EOL)
in order to match. Implementing this requirement as the default behavior
stems primarily from the fact that in the general case it's impossible
to infer with confidence the location of the boundary between
two adjacent numerical values without intervening spaces.
(One exception would be if the data is generated in a standardized format,
say with a constant number of digits after the decimal point;
:issue:`66` aims to address this case.)
This trailing-whitespace requirement was made the default for all tokens
in order to provide a more consistent interface.

However, there are situations... **RESUME**

**WRITE THIS** *For space-after, prob just link to that tutorial page?*



