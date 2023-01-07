#       Day 16: Sum the List
# Write a function called sum_list with one parameter that takes 
# a nested list of integers as an argument and returns the sum of 
# the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
# as an argument your function should return a sum of 33.
#       Extra Challenge: Unpack A Nest
nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from 
# the nested list above – 34, 67, 78. Your output should be another 
# list:
# [34, 67, 78]. The list output should not have duplicates.

def sum_list(list):
     return sum([sum(x) for x in list])

def unpack_nest(list):
    return [list[0][1], list[0][-1], list[1][-1]]

if __name__ == '__main__':
    print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
    print(unpack_nest(nested_list))
