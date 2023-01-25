#       Day 35: Pangram
# Write a function called check_pangram that takes a string 
# and checks if it is a pangram. A pangram is a sentence that 
# contains all the letters of the alphabet. If it is a pangram, 
# the function should return True, otherwise, return False. The 
# following sentence is a pangram so it should return True:
pangram = 'the quick brown fox jumps over a lazy dog'
nonpangram = 'Hello there!'
#       Extra Challenge: Find my Position
# Write a function called find_index that takes two arguments; 
# a list of integers, and an integer. The function should return the 
# indexes of the integer in the list. If the integer is not in the list, 
# the function should convert all the numbers in the list into the 
# given integer. 
# For example, if the list is: 
list = [1, 2, 4, 6, 7, 7] 
# and the integer is 7, 
# your code should return [4, 5] as the indexes of 7 in the list. If 
# the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should 
# return [8, 8, 8, 8, 8, 8] because 8 is not in the list.
import string

def check_pangram(str):
    alphabet = set(string.ascii_lowercase)
    return set(str.lower()) >= alphabet 

def find_index(list, int):
    if int not in list:
        return [int for x in list]
    return [i for i, x in enumerate(list) if x == int]

print(check_pangram(pangram))
print(find_index(list,7))