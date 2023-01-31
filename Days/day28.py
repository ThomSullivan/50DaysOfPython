#       Day 28: Return Indexes
# Write a function called index_position. This function takes a 
# string as a parameter and returns the positions or indexes of all 
# lower letters in the string. For example, ‘LovE’ should return 
# [1,2].
#       Extra Challenge: Largest Number
# Write a function called largest_number that takes a list of 
# integers and re-arrange the individual digits to create the largest 
# number possible. For example, if you pass the following as an 
# argument: 
list1 = [3, 67, 87, 9, 2]# Your code should return the 
# number in this exact format: 9,877,632 as the largest number. 

def index_position(str):
    return [str.index(x) for x in str if x.islower()]

def largest_number(list):
    numbers = ''.join(str(e) for e in list)
    #Cast to string and back to list to seperate multi number, numbers.
    splitNumbers = [ int(x) for x in numbers]
    splitNumbers.sort(reverse=True)
    return (f"{int(''.join(str(e) for e in splitNumbers)):,d}")

print(index_position('LovE'))
print(largest_number(list1))