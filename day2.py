#       Day 2: Strings to Integers
# Write a function called convert_add that takes a list of strings 
# as an argument and converts it to integers and sums the list. For 
example =  ['1', '3', '5'] #should be converted to [1, 3, 5] and
# summed to 9.
#       Extra Challenge: Duplicate Names
# Write a function called check_duplicates that takes a list of 
# strings as an argument. The function should check if the list has 
# any duplicates. If there are duplicates, the function should return 
# the duplicates. If there are no duplicates, the function should 
# return "No duplicates". For example, the list of fruits below 
# should return apple as a duplicate and list of names should 
# return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def convert_add(list):
    base = [int(x) for x in list]
    total = 0
    for i in base:        
        total += i
    return total    

print(convert_add(example))

def check_duplicates(list):
    marker = set()
    dup = {x for x in list if x in marker or (marker.add(x) or False)}
    if len(dup) > 0:
        return dup
    else:
        return 'No duplicates'
    
print(check_duplicates(fruits))
print(check_duplicates(names))