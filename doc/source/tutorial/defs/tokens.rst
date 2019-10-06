.. Token-level semantics

Nomenclature and Definitions: Tokens
====================================

``pent`` understands four kinds of tokens, which match varying types of content.
One is an 'any' token, which matches an arbitrary span of whitespace and/or
non-whitespace content. The other three types are intended to match specific kinds of
content within the line of text that are often, but not always,
separated from surrounding content by whitespace.

All four kinds of tokens accept a flag that instructs the encapsulating
|Parser| to capture the content matching the token for output.
A subset of the tokens accept a flag that
alters how the |Parser| handles the presence or absence of whitespace
following the content matching the token.


The 'Any' Token: |cour|\ ~\ |/cour|
-----------------------------------

The 'any' token will match **anything**, including a completely blank line.
It behaves essentially the same as |cour|\ .*\ |/cour| in regex.

Currently, the 'any' token only accepts the 'capturing' flag
(|cour|\ ~!\ |/cour|). Addition of support for the
'space-after' flags is planned (:issue:`78`).

Note that any content matched by a capturing 'any' token will be
split at whitespace in |Parser| output.


The 'Misc' Token: |cour|\ &\ |/cour|
------------------------------------

The 'misc' token matches any sequence of non-whitespace characters.
Its uses are similar to the 'any' token, except that its match
is confined to a single whitespace-delimited piece of content.
It is mainly intended for use on variable, non-numerical data,
where the 'literal' token cannot be used.

The 'misc' token has one required argument, indicating whether
it should match exactly one piece of content
(|cour|\ &.\ |/cour|) or one-or-more pieces of content
(|cour|\ &+\ |/cour|). When matching one-or-more,
the 'misc' token interleaves *required* whitespace
between each reptition.

The 'misc' token accepts both the capturing flag (**DOC LINK**)
and the 'space-after' modifier flags (**DOC LINK**)


The 'Literal' Token: |cour|\ @\ |/cour|
---------------------------------------

The 'literal' token matches an *exact* sequence of one or more
whitespace-delineated characters, provided as a required argument
in the token definition.

Similar to the 'misc' token, the 'literal' token also has
the quantity specifier as a required argument:
either |cour|\ @.\ |/cour| for exactly one match
or |cour|\ @+\ |/cour| for one-or-more matches.

The argument for the string to be matched follows the
quantity argument. Thus, to match the text
|cour|\ foo\ |/cour| exactly once a suitable token
might be "|cour|\ @.foo\ |/cour|".

In the situation where it's needed to match a literal string
containing a space, the entire token can be enclosed in
quotes: "|cour|\ '@.this has spaces'\ |/cour|".

The 'literal' token differs from the 'misc' and 'number' tokens
in that when the one-or-more argument is used, it does **not**
interleave required whitespace between the repetitions.
This allows, e.g., a long sequence of hyphens to be represented
by a token like |cour|\ @+-\ |/cour|. Similarly, a long
sequence of alternating hyphens and spaces could be represented
by "|cour|\ '@+- '\ |/cour|".


The 'Number' Token: |cour|\ #\ |/cour|
--------------------------------------

The 'number' token allows for selectively matching numbers of varying
types in the text being parsed; in particular, matches can be constrained 
by sign (positive, negative, or either) or by format
(integer, float, or scientific notation; or, combinations of these).

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
   |cour|\ #[.+][.-+]g\ |/cour| for general (integer or float). |br|
   |nbsp|

**FIX THIS** *Different number matchings are implemented because
sometimes (often?) numbers in different formats have different
semantic significance, and it's useful to be able to filter/capture
based on format.*

As with the 'misc' token, when matching in one-or-more quantity mode,
the 'number' token interleaves *required* whitespace between each reptition.

The 'number' token accepts both the capturing flag (**DOC LINK**)
and the 'space-after' modifier flags (**DOC LINK**).


Token Flags
-----------

Capturing Flag: |cour|\ !\ |/cour|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**WRITE THIS** *Capturing*


Space-After Flags: |cour|\ o\ |/cour| and |cour|\ x\ |/cour|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**WRITE THIS** *For space-after, prob just link to that tutorial page?*



