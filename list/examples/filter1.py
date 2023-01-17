list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = []

for item in list1:
    if item % 2 == 0:
        filtered_list.append(item)
        
print(filtered_list)
