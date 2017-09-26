# backwards - Reverse the input iterable and return it
fruit1 = ['apple', 'banana', 'peach']
print(fruit1)
fruit1.reverse()
print(fruit1)
print()

# maximus- Find the max number in a given list. Then, change every element
# in the list containing the first number of the maximum to the maximum number.
num_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
max_num = max(num_list)
first_num = int(str(max_num)[0])
num_list2 = []
for num in num_list:
    if str(first_num) in str(num):
        num_list2.append(max_num)
    else:
        num_list2.append(num)
print(num_list)
print(max_num)
print(num_list2)
print()

# compare_first_element - Given two lists, return True of the first two items are the equal.
fruit1 = ['apple', 'banana', 'peach']
fruit2 = ['apple', 'plum', 'cherry']

def compare_first_element(list1, list2):
    if fruit1[0] == fruit2[0]:
        return True
    else:
        return False

print(compare_first_element(fruit1, fruit2))
print()

# compare_second_letter - Return True if the first letter of the second element
# in each list is equal. (Case Insensitive)
fruit1 = ['apple', 'banana', 'peach']
fruit2 = ['apple', 'plum', 'cherry']

def compare_first_element(list1, list2):
    if fruit1[1] == fruit2[1]:
        return True
    else:
        return False

print(compare_first_element(fruit1, fruit2))
print()


# smoosh - Given two lists, return one list, with all of the items of the first
# list, then the second. Use a default argument to allow the user to reverse the order!
fruit1 = ['apple', 'banana', 'peach']
fruit2 = ['apple', 'plum', 'cherry']

all_fruit = (fruit1 + fruit2)
print(all_fruit)
all_fruit.reverse()
print(all_fruit)
