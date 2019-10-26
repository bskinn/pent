.. pent mini-language grammar

pent Mini-Language Grammar
==========================

As discussed :doc:`here </tutorial/basics>`, a ``pent`` |Parser|
is constructed by passing it *patterns* composed of *tokens*. The grammar below
specifies what constitutes a valid ``pent`` *token*.

For completeness, even though the
:ref:`optional-line pattern flag <tutorial-basics-patterns-optionallineflag>`
is called a *flag* and not a *token*, internally ``pent`` parses this flag
as though it were a token, and thus it is included here.

This grammar is expressed in an approximation of
`extended Backus-Naur form <https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form>`__.
Content in double quotes represents a literal string, the pipe character indicates alternatives,
square brackets indicate *optional* token flags, and parentheses indicate *required* token flags.

**Grammar**

.. code-block:: none

    token                   ::=  optional_line_flag | content_token

    optional_line_flag      ::=  "?"
    content_token           ::=  any_token | literal_token | misc_token | number_token

    any_token               ::=  "~"[capture]
    literal_token           ::=  "@"[space_after][capture](quantity)(literal_content)
    misc_token              ::=  "&"[space_after][capture](quantity)
    number_token            ::=  "#"[space_after][capture](quantity)(sign)(num_type)

    space_after             ::=  optional_space_after | no_space_after
    optional_space_after    ::=  "o"
    no_space_after          ::=  "x"

    capture                 ::=  "!"

    quantity                ::=  match_one | match_one_or_more
    match_one               ::=  "."
    match_one_or_more       ::=  "+"

    sign                    ::=  any_sign | positive_sign | negative_sign
    any_sign                ::=  "."
    positive_sign           ::=  "+"
    negative_sign           ::=  "-"

    num_type                ::=  integer | decimal | sci_not | float | general
    integer                 ::=  "i"
    decimal                 ::=  "d"
    sci_not                 ::=  "s"
    float                   ::=  "f"
    general                 ::=  "g"


