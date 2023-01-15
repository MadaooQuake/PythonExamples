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

Python allows us to apply a transform function (for example square of each item) to every item 
in an iterable object by the map function, like:

```
>>> some_list = [1, 4, 7, 10, 20]
```

* square numbers
```
def square_number(number):
    return number ** 2

>>> squared_numbers_of_list = map(square_number, some_list)
```
Remember that the map() function returns a map object (an iterator) and you have to apply another
function like list or tuple to get the result in digital format

```
>>> print(list(squared_numbers_of_list))
[1, 16, 49, 100, 400]
```

* adding numbers using map and lambda

```
>>> added_numbers = map(lambda x: x + x, some_list)
>>> print(list(added_numbers))
[2, 8, 14, 20, 40]
```

* adding two lists using map and lambda

```
>>> another_list = [1, 4, 7, 10, 20]
>>> added_lists = map(lambda x, y: x + y, some_list, another_list)
>>> print(list(added_lists))
[2, 8, 14, 20, 40]
```

* converting string numbers to int

```
>>> some_list = ["1", "4", "7", "10", "20"]
>>> str_to_int_nums = map(int, some_list)
>>> print(list(str_to_int_nums))
[1, 4, 7, 10, 20]
```

* string manipulation

```
>>> some_list = ["anna", 'has', 'a', 'cat']
>>> print(list(map(str.capitalize, some_list)))
['Anna', 'Has', 'A', 'Cat']
```

```
>>> some_list = ["     anna", 'has', 'a    ', '    cat']
>>> print(list(map(str.strip, some_list)))
['anna', 'has', 'a', 'cat']
```

when you want to strip by special character (for example comma) then you need to using lambda operator

```
>>> some_list = ["     anna,", 'has', ', a    ', '    cat']
>>> print(list(map(lambda s: s.strip(','), some_list)))
['     anna', 'has', ' a    ', '    cat']
```

It is common to use the map() function with the reduce() and the filter() functions.

## The Zip() function

## Check for Uniqueness

## Checking memory usage of the list
