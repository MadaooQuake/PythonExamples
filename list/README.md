# Useful operations on lists
- [Useful operations on lists](#useful-operations-on-lists)
  - [Introdution](#introdution)
  - [Merge lists](#merge-lists)
  - [The Filter() Function](#the-filter-function)
  - [List Comprehensions](#list-comprehensions)
  - [The Map() Function](#the-map-function)
  - [The Zip() functions](#the-zip-functions)
  - [Check for Uniqueness](#check-for-uniqueness)
  - [Checking memory usage of the list](#checking-memory-usage-of-the-list)

## Introduction
The article is devoted to list operations that will make it easier for us to handle them.
Generaly using list in Python Language is very popular and somethimes We implement complicated 
algorithm for merging list, filter some elements in list or find something in list. 

So this article is so that we don't have to invent advanced algorithms,
but already use ready-made mechanisms to handle lists in Python. 

## Merge lists

## The Filter() function

## List Comprehensions

## The Map() function

## The Zip() function

## Flatten a list of lists

Very often we get a complex structure as the output of some operation. One of the case is list of lists.
Python lets us to convert a list of lists into a single list using list comprehension in a simple manner.
```
>>> list_of_lists = [[1, 2],
                     [3, 4],
                     [5, 6],
                     [7, 8],
                     [9, 10]]

single_list = [item for internal_list in list_of_lists for item in internal_list]
```

instead of
```
single_list = []
for internal_list in list_of_lists:
    for item in internal_list:
        single_list.append(item)
```

you can do this also using functools, reduce and operator.iconcat
```
>>> import functools
>>> import operator

>>> print(functools.reduce(operator.iconcat, list_of_lists, []))
```
or just using itertools.chain

```
>>> import itertools

>>> print(list(itertools.chain(*list_of_lists)))
```

## Check for Uniqueness

## Checking memory usage of the list
