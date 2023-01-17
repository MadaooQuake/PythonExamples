list1 = ['beaver', 'lemon', 'beard', 'cat', 'dog']

def check_even(word):
    if 'b' in word:
          return True  
    return False
        
filtered_list = list(filter(check_even, list1))
print(filtered_list)
