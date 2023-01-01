#       Day 11: Are They Equal?
# Write a function called equal_strings. The function takes two 
# strings as arguments and compares them. If the strings are equal 
# (if they have the same characters and have equal length), it 
# should return True, if they are not, it should return False. For 
# example, ‘love’ and ‘evol’ should return True.
#       Extra Challenge: Swap Values
# Write a function called swap_values. This function takes a list 
# of numbers and swaps the first element with the last element. 
# For example, if you pass [2, 4,67, 7] as a parameter, your 
# function should return
# [7, 4, 67, 2].

def equal_strings(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

def swap_values(list):
    newList = list.copy()
    newList[0], newList[-1] = list[-1], list[0]
    return newList

if __name__ == "__main__":
    oldList = [2, 4, 67, 7]
    print(equal_strings('love', 'evol'))
    print(swap_values(oldList))