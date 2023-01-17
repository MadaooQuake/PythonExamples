list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7, 8]

merged_list = list1

for item in list2:
    if item not in merged_list:
        merged_list.append(item)

print(merged_list)
