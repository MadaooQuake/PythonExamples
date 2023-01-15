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

## List Comprehensions

## The Map() Function

## The Zip() functions

## Check for Uniqueness

## Checking memory usage of the list