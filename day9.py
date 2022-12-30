#       Day 9: Biggest Odd Number
# Create a function called biggest_odd that takes a string of 
# numbers and returns the biggest odd number in the list. For 
# example, if you pass ‘23569’ as an argument, your function 
# should return 9. Use list comprehension.
#       Extra Challenge: Zeros to the End
# Write a function called zeros_last. This function takes a list as 
# argument. If a list has zeros (0), it will move them to the front of 
# the list and maintain the order of the other numbers in the list. 
# If there are no Zeros in the list, the function should return the 
# original list sorted in ascending order. For example, if you pass 
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1, 
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument, 
# your code should return [1, 2, 4, 6, 7].

def biggest_odd(str):
    return max([int(x) for x in str if int(x) % 2 != 0])

def zeros_last(list):
    func_list = list.copy()
    if 0 not in func_list:
        func_list.sort()
    else:
        for i in range(len(func_list)):
            if func_list[i] != 0:
                pass
            else:
                func_list.pop(i)
                func_list.append(0)
    return func_list

input = [2,1,4,7,6]
input2 = [1,4,6,0,7,0,9]
print(zeros_last(input2))

