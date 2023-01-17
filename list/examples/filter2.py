list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  
    return False
        
filtered_list = list(filter(check_even, list1))
print(filtered_list)
