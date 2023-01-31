#        Day 3: Register Check
# Write a function called register_check that checks how many 
# students are in school. The function takes a dictionary as a 
# parameter. If the student is in school, the dictionary says ‘yes’. If 
# the student is not in school, the dictionary says ‘no’. Your 
# function should return the number of students in school. Use the 
# dictionary below. Your function should return 3.
register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

#       Extra Challenge: Lowercase Names 
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam", "zuul"]
# You are given a list of names above. This list is made up of names 
# of lowercase and uppercase letters. Your task is to write a code 
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted 
# alphabetically in descending order. Using the list above, your 
# code should return:
# ('kerry', 'dickson', 'carol', 'adam')

def register_check(dict):
    total = 0
    for key, value in dict.items():
        if value == 'yes':
            total += 1
        else:
            pass
    return total  

print(register_check(register))

def lowercase_check(list):
    result = []
    for i in list:
        if i.islower():
            result.append(i)
        else:
            pass
    result.sort(reverse=True)
    return tuple(result)

print(lowercase_check(names))