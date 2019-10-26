.. pent parser tutorial

pent Parser Tutorial
====================

There is almost always more than one way to construct a ``pent`` |Parser|
to capture a given dataset. Sometimes, if the data
format is complex or contains irrelevant content interspersed with the
data of interest, significant pre- or post-processing may be required. As well,
it's important to inspect your starting data carefully, often by
loading it into a Python string, to be sure there aren't, say, a bunch of
unprintable characters floating around and fouling the regex matches.

This tutorial starts by describing the basic structure of
the semantic components of ``pent``'s parsing model:
*tokens*, *patterns*, and |Parsers|.
It then lays out some approaches to constructing |Parsers|
for realistic datasets, with the goal of enabling new users
to get quickly up to speed
building their own |Parsers|.

For a formal description of the
grammar of the tokens used herein, see the
:doc:`grammar`.


.. toctree::
    :maxdepth: 2

    tutorial/basics
    tutorial/examples

