.. pent documentation master file, created by
   sphinx-quickstart on Mon Sep  3 21:50:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pent!
================

A common frustration in data analysis is software tooling
that *only* generates its output in human-readable fashion. Thus,
even if there is visible structure to the data, that structure is
embedded in a format that can be awkward to parse.

Take the following toy data:

.. doctest:: toy

    >>> text = """{lots of content}
    ...
    ...           $data1
    ...           0     0.000
    ...           1    -3.853
    ...           2     1.219
    ...
    ...           $data2
    ...           0     3.142
    ...           1     2.718
    ...           2     6.022
    ...
    ...           {lots more content}"""

Say it's needed to extract the list of decimal values in
|cour|\ $data1\ |/cour|, *without* the accompanying integers.
Further, say that in any given particular output file,
this list of values can be of *any* length.

One could write a line-by-line search to parse out the values,
but that's a slow way to go about it if there are many such data blocks
that need to be extracted.

Regex is a pretty natural tool to use here, but writing the regex
to retrieve these values is a non-trivial task: because of the way
regex capture groups work, you really have to write *two* regexes.
The first regex captures the whole chunk of text of interest,
and the second searches within that chunk to capture the values
from the individual lines.

``pent`` **writes all this regex for you.**

All you have to do is provide ``pent`` with the structure of
the text using its custom mini-language,
including which parts should be captured for output,
and it will scrape the data directly from the text:

.. doctest:: toy

    >>> prs = pent.Parser(
    ...     head="@.$data1",
    ...     body="#.+i #!..d",
    ... )
    >>> prs.capture_body(text)
    [[['0.000'], ['-3.853'], ['1.219']]]

This is just one example of ``pent``\ 's parsing
capabilities---it's an extremely flexible tool, which can retrieve
just about anything you want from just about any
surrounding text.

``pent`` is available on PyPI, and thus can be installed
via "|cour|\ pip install pent\ |/cour|".

Usage instructions for ``pent`` are provided in the
:doc:`tutorial </tutorial>`, broken up into
(1) an explanation of the
:doc:`basics </tutorial/basics>` of the syntax
and (2) exposition of a number of
(more-)realistic :doc:`examples </tutorial/examples>`.
For those so inclined, a formal grammar of
the mini-language is also :doc:`provided </grammar>`.

What ``pent`` is not
--------------------

``pent`` is **not** well suited for parsing data with an extensively
nested or recursive structure, especially if that structure
is defined by clear rules. Have JSON, XML, or YAML? There are other
libraries specifically made for those formats, and you should use them.
``pent`` ultimately is just a fancy regex generator, and thus it
carries the same functional constraints. If you build a |Parser|
that is too complex, it *will* run until approximately
the heat death of the universe!


**Contents:**

.. toctree::
    :maxdepth: 1

    tutorial
    grammar
    api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
