#       Day 27: Unique Numbers
# Write a function called unique_numbers that takes a list of 
# numbers as an argument. Your function is going to find all the 
# unique numbers in the list. It will then sum up the unique 
# numbers. You will calculate the difference between the sum of 
# all the numbers in the original list and the sum of unique 
# numbers in the list. If the difference is an even number, your 
# function should return the original list. If the difference is an 
# odd number, your function should return a list with unique 
# numbers only. For example 
list = [1, 2, 4, 5, 6, 7, 8, 8]  
# should return [1, 2, 4, 5, 6, 7, 8, 8].
#       Extra Challenge: Difference of two Lists
# Write a function called difference that takes two lists as 
# arguments. This function should return all the elements that are 
# in list a but not in list b and all the elements in list b not in list 
# a. For example:
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]
# Use list comprehension in your function.


def unique_numbers(list):
    num_set = set(list)
    if (sum(list) - sum(num_set)) % 2 != 0:
        return [i for i in set(num_set)]
    return list
    
def difference(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(unique_numbers(list))
print(difference(list1, list2))
