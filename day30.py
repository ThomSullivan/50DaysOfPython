#       Day 30: Most Repeated Name
# Write a function called repeated_name that finds the most 
# repeated name in the following list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
 
#       Extra Challenge: Sort by Last Name
# You work for a local school in your area. The school has a list of 
# names of students saved in a list. The school has asked you to 
# write a program that takes a list of names and sorts them
# alphabetically. The names should be sorted by last names. Here 
# is a list of names:
names =  ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown',' Tom Cruise']
# Your code should not just sort them alphabetically, but it should 
# also switch the names (the last name must be the first). Here is 
# how your code output should look:
# ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyonce', 'Perry Katie' ]
# Write a function called sorted_names.

def repeated_name(list):
    names = {}
    for name in list:
        if name not in names.keys():
            names[name] = 1
            continue
        names[name] += 1
    return max(names, key=names.get)

def sorted_names(list):
    newList = []
    for name in list:
        firstAndLast = name.split()
        firstAndLast.reverse()
        ' '.join(firstAndLast)
        newList.append(' '.join(firstAndLast))
    newList.sort()    
    return newList

print(repeated_name(name))
print(sorted_names(names))