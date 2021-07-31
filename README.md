# Session 12 Assignment on Iterables and Iterators II

An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over


In this assignment, we try to understand the concept of lazy iterators which loads only required information in every iteration and doesnt load all the enitre data at once.

## Assignment Description:

We have created 2 classes Polygon and polysequence (from previous sessions) and the current assignment has 2 Goals:

Goal 1 -  Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

Goal - 2 - Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

The Jupyter Notebook is also uploaded into this repository (NotebookSession12.ipynb)
