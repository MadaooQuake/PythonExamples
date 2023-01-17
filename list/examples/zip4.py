list_zip = [(1, 'I', 'four'), (2, 'II', 'two'), (3, 'III', 'one'), (4, 'IV', 'three')]

list1, list2, list3 = list(zip(*list_zip))

print(list1)
print(list2)
print(list3)
