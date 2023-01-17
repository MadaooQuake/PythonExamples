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

Python can merge lists with each other in a variety of ways. In this section we will go through the most popular ways to
merge lists and which are offered by the latest version of Python.

The first way, which is simple, we will use a plus for combining lists:
```
list1 = [1,2,3,4]
list2 = [5,6,7,8]

merged_list = list1 + list2
print(merged_list)
```
Example 1 output:
```
[1, 2, 3, 4, 5, 6, 7, 8]
```
 
We will modify the above example a bit:
```
list1 = [1,2,3,4]
list2 = [4,5,6,7,8]

merged_list = list1 + list2
print(merged_list)
```
Example 2 output:
```
[1, 2, 3, 4, 4, 5, 6, 7, 8]
```
In cases where we do not want repetition after merging lists, this method will unfortunately not work.

Since Python 3.5, you can alternatively concatenate lists using [*list1 , *list2]. 
```
list1 = [1,2,3,4]
list2 = [5,6,7,8]

merged_list = [*list1, *list2]
print(merged_list)
```
Unfortunately, this way is also not suitable for merging lists without repetition. 

We can use the extend() function to merge lists:
```
list1 = [1,2,3,4]
list2 = [5,6,7,8]

merged_list = []
merged_list.extend(list1)
merged_list.extend(list2)

print(merged_list)
```
Of course, it is also unsuitable in case you do not want to have duplicates.

Now I will do the old way of merging lists with each other, so that there is no repetition. 
```
list1 = [1,2,3,4]
list2 = [4,5,6,7,8]

merged_list = list1

for item in list2:
    if item not in merged_list:
        merged_list.append(item)

print(merged_list)
```
And a nicer way to merge lists:
```
list1 = [1,2,3,4]
list2 = [4,5,6,7,8]

merged_list = list(set(list1 + list2))
print(merged_list)
```
The set function has been with us since python 2 but unfortunately it is rarely seen in use, and it can really simplify list merging for us when we don't want to have repetition. 

## The Filter() Function

The filter() function, as the name suggests, is used to filter data in lists. 
The feature has been with us since Python version 2, but many people continue not to use it.

Below is an example without using the filter function:
```
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = []

for item in list1:
    if item % 2 == 0:
        filtered_list.append(item)
        
print(filtered_list)
```
Output:
```
[2, 4, 6, 8, 10]
```

Now code with use the filter function:
```
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  
    return False
        
filtered_list = list(filter(check_even, list1))
print(filtered_list)
```
Output is the same. 

The filter function can be applied not only to numbers, but it can filter anything we want from the list. Below is the code to check if filtering by the letter b:
```
list1 = ['beaver', 'lemon', 'beard', 'cat', 'dog']

def check_even(word):
    if 'b' in word:
          return True  
    return False
        
filtered_list = list(filter(check_even, list1))
print(filtered_list)
```
Output:
```
['beaver', 'beard']
```

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

The Zip() function in Python serves to create Tuple object. The Zip() function as parameter use Lists, strings, numbers, tuple, etc. 
The Zip() function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
The following example, using the zip() function, creates a tuple object from two lists:
```
list1 = ["one", "two", "three", "four"]
list2 = [1,2,3,4]
zip_object = zip(list1, list2)

#zip object
print(zip_object)

# print tuple as a list
print(list(zip_object))
```
output:
```
<zip object at 0x7fdb86086500>
[('one', 1), ('three', 2), ('four', 3), ('two', 4)]
```
You can also convert a tuple object to a list, as seen in the example above. 
Whether the zip function can accept more parameters than two, we will check: 
```
list1 = [1,2,3,4]
list2 = ["I", "II", "III", "IV"]
list3 = ["one", "two", "three", "four"]

list_zip = zip(list1, list2, list3)
print(list(list_zip))
```
As you can see it can be quietly done, and here is the result of our combination of three lists:
```
[(1, 'I', 'four'), (2, 'II', 'two'), (3, 'III', 'one'), (4, 'IV', 'three')]
```
We can also zipped list with diffrent lenght:
```
list1 = [1,2]
list2 = ["one", "two", "three", "four"]

list_zip = zip(list1, list2)
print(list(list_zip))
```
Output:
```
[(1, 'four'), (2, 'one')]
```
In this case, the zip function as it does not see that something can no longer connect, it rejects. 

We can also reverse the result of the zip function.
```
list_zip = [(1, 'I', 'four'), (2, 'II', 'two'), (3, 'III', 'one'), (4, 'IV', 'three')]

list1, list2, list3 = list(zip(*list_zip))

print(list1)
print(list2)
print(list3)
```
Output:
```
(1, 2, 3, 4)
('I', 'II', 'III', 'IV')
('four', 'two', 'one', 'three')
```

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

* for

You can find out if the list is unique by using simply for loop:

```
>>> elements = []
>>> for element in some_list:
        if element in elements:
            print('list {some_list} is not unique')
            break
        elements.append(element)
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

To check memory usage of the list you can use sys module.

sys.getsizeof return the size of an object in bytes. According to the documentation 
"Only the memory consumption directly attributed to the object is accounted for".
Moreover the size of the memory contains garbage collector overhead.

Using Python 3.11 on Windows I see the following result:

```
>>> import sys
>>> some_list = []
>>> sys.getsizeof(some_list)
56
```
So, the empty list object is about 56 B. 

```
>>> some_list = [1]
>>> sys.getsizeof(some_list)
64

>>> some_list = ['1']
>>> sys.getsizeof(some_list)
64
```

The one-element list object is about 64 B regardless of the type of element (int or str).
The result is expected as in case of the list there are pointers to values 
and each is 8 bytes (64 bit python).
So 1 element = one 8-bytes pointer.
56 + 8 = 64 as we expect.

```
>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8]
>>> sys.getsizeof(some_list)
120

>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> sys.getsizeof(some_list)
168

>>> some_list = [x for x in range(1000)]
>>> sys.getsizeof(some_list)
8856
```
It is really good to know that in CPython the memory is preallocated in chunks to avoid 
extending the list too frequently due to fact that resize operation is really costly 
and it should be done rarely. 
So as you can see:

```
>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8]
>>> sys.getsizeof(some_list)
120
>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sys.getsizeof(some_list)
136
>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> sys.getsizeof(some_list)
136
>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> sys.getsizeof(some_list)
152
```
sometimes we can observe that the size of memory doesn't change.

Another example of preallocating the memory you can see below:

```
>>> some_list = []
>>> sys.getsizeof(some_list)
56
>>> some_list = [1]
>>> sys.getsizeof(some_list)
64
>>> some_list = [1, 2]
>>> sys.getsizeof(some_list)
72
>>> some_list = [1, 2, 3]
>>> sys.getsizeof(some_list)
88
```

As you can see at beginning the list has allocated 56 bytes. After creating 1- and 2-elements lists
there are allocated next 8 and 16 bytes as expected. 
But when the list has 3 elements then Python allocates 88 bytes so twice as much as we expected. 
It follows from preallocating mechanism of Python.

In case of remove elements from the list using pop() method Python will shrink it in case of 
removing more then half of the items.
The example is shown below:

```
>>> some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> sys.getsizeof(some_list)
136
>>> some_list.pop()
10
>>> sys.getsizeof(some_list)
136
>>> some_list.pop()
9
>>> sys.getsizeof(some_list)
136
>>> some_list.pop()
8
>>> sys.getsizeof(some_list)
136
>>> some_list.pop()
7
>>> sys.getsizeof(some_list)
136
>>> some_list.pop()
6
>>> sys.getsizeof(some_list)
136
>>> some_list.pop()
5
>>> sys.getsizeof(some_list)
120
```

As you can see, only when 5-th element is popped then Python shrinks the allocated memory.
