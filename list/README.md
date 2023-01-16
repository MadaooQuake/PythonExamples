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
Lists are programming structures available in every programming language.
Generally speaking, list is one of the most commonly used structures in Python Language and sometimes we implement complicated 
algorithm for merging list, filter some elements in list or find something in list.
So t is therefore profitable to know them - in case of basic programming and also during advanced algorithms.

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

Python's lists can contain elements which are not unique. So you can have the following list:

```
>>> some_list = [1, 1, 2, 3, 4, 4]
```

Sometimes it is required to know if the list has unique elements or not. 
You can do this in different ways.

* set

A Python's set data structure is an unordered structure with unique elements.
So, comparing the length of the list and the set you can check if the list has unique values or not.

```
>>> some_list = [1, 1, 2, 3, 4, 4]
>>> len(some_list) == len(set(some_list))
False
```

* count

The in-built count() method allows us to count the frequency of each element of the list. 
If the count value is grater than 1 then there are duplicates.

```
>>> some_list = [1, 1, 2, 3, 4, 4]
>>> for element in set(some_list):
        print(f'element: {element}, count: {some_list.count(element)}')

element: 1, count: 2
element: 2, count: 1
element: 3, count: 1
element: 4, count: 2
```

## Checking memory usage of the list
