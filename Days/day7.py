#       Day 7: A String Range
# Write a function called string_range that takes a single 
# number and returns a string of its range. The string characters 
# should be separated by dots(.) For example, if you pass 6 as 
# an argument, your function should return ‘0.1.2.3.4.5’.
#       Extra Challenge: Dictionary of names
# You are given a list of names, and you are asked to write a code 
# that returns all the names that start with ‘S’. Your code should 
# return a dictionary of all the names that start with S and how 
# many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", 'Sera' , "Patel" , 'Sera']
# Your code should return: {“Sasha”: 1, “Sera”: 2}
from collections import defaultdict

def string_range(num):
    value = [str(x) for x in range(num)]
    return '.'.join(value)

print(string_range(6))

def find_s(list):
    value = defaultdict(int)
    for i in list:
        if i[0].casefold() != 's':
            pass   
        else:
            value[i] += 1         
    return dict(value)

print(find_s(names))