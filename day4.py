#       Day 4: Only Floats
# Write a function called only_floats, which takes two 
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither 
# argument is a float. If you pass (12.1, 23) as an argument, your 
# function should return a 1.
#       Extra Challenge: Index of the Longest Word
# Write a function called word_index that takes one argument, 
# a list of strings and returns the index of the longest word in the 
# list. If there is no longest word (if all the strings are of the same 
# length), the function should return zero (0). For example, the list 
# below should return 2.
words1 = ["Hate", "remorse", "vengeance"]
#  And this list below, shoul return zero (0)
words2 = ["Love", "Hate"]

def only_floats(num1,num2):
    total = 0 
    if isinstance(num1, float):
        total += 1
    if isinstance(num2, float):
        total += 1
    else:
        pass
    return total

print(only_floats(12.1, 23))

def word_index(list):
    base = [len(x) for x in list]
    max_value = max(base)
    return base.index(max_value)

print(word_index(words1))
print(word_index(words2))