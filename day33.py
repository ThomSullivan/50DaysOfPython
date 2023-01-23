#       Day 33: List Intersection
# Write a function called inter_section that takes two lists and 
# finds the intersection (the elements that are present in both 
# lists). The function should return a tuple of intersections. Use 
# list comprehension in your solution. Use the lists below. Your 
# function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
#       Extra Challenge: Set or list
# You want to implement a code that will search for a number in 
# a range. You have a decision to make as to whether to store the 
# number in a set or a list. Your decision will be based on time. 
# You have to pick a data type that executes faster.
# You have a range and you can either store it in a set or a list
# depending on which one executes faster when you are searching 
# for a number in the range. See below:
a = range(10000000)
x = set(a)
y = list(a)
# Let’s say you are looking for a number 9999999 in the range 
# above. Search for this number in the list and the set. Your 
# challenge is to find which code executes faster. You will pick the 
# one that executes quicker, lists, or sets. Run the two searches 
# and time them
import timeit

def inter_section(list1, list2):
    return tuple( x for x in list1 if x in list2)

print(inter_section(list1,list2))

print('{} seconds to find in a list'.format(timeit.timeit('filter(9999999,y)',setup='y = list(range(10000000))')))

print('{} seconds to find in a set'.format(timeit.timeit('9999999 in y',setup='y = set(range(10000000))')))


