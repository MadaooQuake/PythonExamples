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

List comprehension is a simple and useful mechanism to reduce a multiline code into a smaller one. 
It is a shorter syntax to create a new list based on the existing one.

Instead of writing 3-lines for loop like:

```
>>> some_list = ["anna", 'has', 'a', 'cat', 'and', 'a', 'dog']
>>> animals_list = []

>>> for s in some_list:
        if 'cat' in s or 'dog' in s:
            animals_list.append(s)

>>> print(animals_list)
['cat', 'dog']
```
you can write just one-line list comprehension:
```
>>> animals_list = [s for s in some_list if 'cat' in s or 'dog' in s]
>>> print(animals_list)
['cat', 'dog']
```

Similarly to the map() function you can do some string manipulation using the list comprehension:

```
>>> some_list = ["anna", 'has', 'a', 'cat']
>>> list_upper = [s.upper() for s in some_list]
>>> print(list_upper)
['ANNA', 'HAS', 'A', 'CAT', 'AND', 'A', 'DOG']
```

Simply if-else statement using the list comprehension may look as follows:

```
>>> animals_list = [s if 'horse' in s else 'wrong word' for s in some_list]
>>> print(animals_list)
['wrong word', 'wrong word', 'wrong word', 'wrong word']
```

You can also iterating through a string using the list comprehension:

```
>>> print([s for s in 'hello'])
['h', 'e', 'l', 'l', 'o']
```

* List comprehension vs for loop

You have to be aware of readibility of solution is very important thing. So sometimes it is better
to write for loop with more lines than ugly and illegible list comprehension.

Moreover we can notice more time-efficient in case of list comprehension than for loop:

```
snippet_comprehension = """
a = range(1000000)
b = [i**2 for i in a]
"""

snippet_for = """
a = range(1000000)
b = []

for i in a:
    b.append(i**2)
"""

>>> elapsed_time = timeit.timeit(snippet_comprehension, number=100)/100
0.0545

>>> elapsed_time = timeit.timeit(snippet_for, number=100)/100
>>> print(elapsed_time)
0.06391431700001704
```

So, as you can see, there is a advantage of list comprehension over for loops even if simple operation like number powering of numbers.

## The Map() function

## The Zip() function

## Check for Uniqueness

## Checking memory usage of the list
