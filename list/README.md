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

## Sorting
Instead of writing sort algorithms by yourself, you can use available in Python sort methods along with some features like ordering, reversing etc
```
some_list = [4, 1, 7, 20, 10]
```

sorting in place - so you change object
```
>>> some_list.sort()
>>> print(some_list)
[1, 4, 7, 10, 20]
```

reverse sorting in place
```
>>> some_list.sort(reverse=True)
>>> print(some_list)
[20, 10, 7, 4, 1]
```

sorting temporarily - so you don't change object
```
>>> print(sorted(some_list))
[1, 4, 7, 10, 20]
```

## Check for Uniqueness

## Checking memory usage of the list
