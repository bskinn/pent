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

This tutorial lays out some approaches to constructing |Parser|\ s
for real-world datasets, with the goal of enabling new users
to get quickly up to speed
building their own |Parser|\ s. For more information about the
specifics of the grammar of the tokens used herein, see the
:doc:`grammar`.


.. toctree::
    :maxdepth: 1

    tutorial/definitions
    tutorial/single_parser
    tutorial/nested_parsers
    tutorial/misc_and_post_processing
    tutorial/internal_spaces
    tutorial/space_after
    tutorial/data_cleanup
