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

## Introdution
The article is devoted to list operations that will make it easier for us to handle them.
Generaly using list in Python Language is very popular and somethimes We implement complicated 
algorithm for merging list, filter some elements in list or find something in list. 

So this article is so that we don't have to invent advanced algorithms,
but already use ready-made mechanisms to handle lists in Python. 

## Merge lists

Python can merge lists with each other in a variety of ways, in this section we will go through the most popular merged lists and which theses are offered by the latest version of Python.

The first way, which is simple, but unfortunately not the best solution.

```
list1 = [1,2,3,4]
list2 = [5,6,7,8]

merged_list = list1 + list2
print(merged_list)
```
Example 1 output :
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
Example 2 output :
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

## The Map() Function

## The Zip() functions

The Zip() function in Python serves to create Tuple object. The Zip() function as paremteter use Lists, strings, numbers, tuple, etc. 
The Zip() function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
The following example, using the zip(0) function, creates a tuple object from two lists:
```
list1 = {"one", "two", "three", "four"}
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

## Checking memory usage of the list