.. ~Glossary of terms, plus some explanation

Basic Usage
===========

``pent`` searches text in a line-by-line fashion,
where a line of text is delimited by the start/end
of the string, and/or by newline(s).

Each line of text to be matched by ``pent`` is represented
by a *pattern*, passed into a |Parser|.
Each *pattern* is a string composed of zero or more whitespace-separated *tokens*,
which define in a structured way what the overall *pattern* should match.
Both *patterns* **and** *tokens*  can also include *flags*,
which modify the semantics of how they are processed.

At present, whitespace is hardcoded to include only spaces and
tab characters (|cour|\ \\t\ |/cour|). Various options for user-configurable
whitespace definition are planned (:issue:`26`).


.. toctree::
    :maxdepth: 1

    Tokens <basics/tokens>
    Patterns <basics/patterns>
    Parsers <basics/parser>


