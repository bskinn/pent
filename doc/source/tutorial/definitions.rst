.. ~Glossary of terms, plus some explanation

Nomenclature and Definitions
============================

**ADD LOTS OF LINKS TO RELEVANT EXAMPLE PAGES FROM THE TUTORIAL!!**

Overall Structure
-----------------

``pent`` searches text in a line-by-line fashion,
where a line of text is delimited by the start/end
of the string, and/or by newline(s).

Each line of text to be matched by ``pent`` is represented
by a *pattern*, passed into a |Parser|.
Each *pattern* is composed of zero or more whitespace-separated *tokens*,
which define in a structured way what the overall *pattern* should match.
Both *patterns* **and** *tokens*  can also include *flags*,
which modify the semantics of how they are processed.

At present, whitespace is hardcoded to include only spaces and
tab characters (|cour|\ \\t\ |/cour|). A user-configurable
whitespace definition is planned (:issue:`NEED THIS`).

*head/body/tail Parser paradigm*


**PROBABLY PUT A TOCTREE HERE, POINTING TO SEPARATE PAGES FOR 
AT LEAST TOKENS AND PATTERNS; MAYBE FLAGS, TOO?**


Tokens
------

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


|cour|\ ~\ |/cour| - The 'Any' Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 'any' token will match **anything**, including a completely blank line.
It behaves essentially the same as |cour|\ .*\ |/cour| in regex.

Currently, the 'any' token only accepts the 'capturing' flag
(|cour|\ !\ |/cour|). Addition of support for the
'space-after' flags is planned (:issue:`CHECK THIS`).

Note that any content matched by a capturing 'any' token will be
split at whitespace in |Parser| output.


|cour|\ &\ |/cour| - The 'Misc' Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

The 'misc' token accepts both the capturing flag (**LINK**)
and the 'space-after' modifier flags (**LINK**)


|cour|\ @\ |/cour| - The 'Literal' Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
quotes: |cour|\ '@.this has spaces'\ |/cour|.

The 'literal' token differs from the 'misc' and 'number' tokens
in that when the one-or-more argument is used, it does **not**
interleave required whitespace between the repetitions.
This allows, e.g., a long sequence of hyphens to be represented
by a token like |cour|\ @+-\ |/cour|. Similarly, a long
sequence of alternating hyphens and spaces could be represented
by |cour|\ '@+- '\ |/cour|.


|cour|\ #\ |/cour| - The 'Number' Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 'number' token allows for selectively matching numbers of varying
types in the text being parsed; in particular, matches can be constrained 
by sign (positive, negative, or either) or by format
(integer, float, or scientific notation; or, combinations of these).

The 'number' token takes three required arguments:

1. Quantity -
   |cour|\ #.\ |/cour| for exactly one, or
   |cour|\ #+\ |/cour| for one-or-more

2. Sign -
   |cour|\ #[.+]+\ |/cour| for positive,
   |cour|\ #[.+]-\ |/cour| for negative, or
   |cour|\ #[.+].\ |/cour| for either sign

3. Number Format -
   |cour|\ #[.+][.-+]i\ |/cour| for integer,
   |cour|\ #[.+][.-+]d\ |/cour| for decimal,
   |cour|\ #[.+][.-+]s\ |/cour| for scientific notation,
   |cour|\ #[.+][.-+]f\ |/cour| for float (decimal or scinot)
   |cour|\ #[.+][.-+]g\ |/cour| for general (integer or float)

**MORE STUFF HERE**

*Pattern examples*



*Capturing*

*For space-after, prob just link to that tutorial page?*


- Number tokens
- Misc tokens
- Literal tokens
- Any token
- Optional flag
- Capturing
- Space-after

