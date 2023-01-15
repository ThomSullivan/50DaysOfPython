#       Day 25: All the Same
# Create a function called all_the_same that takes one 
# argument, a string, a list, or a tuple and checks if all the 
# elements are the same. If the elements are the same, the function 
# should return True. If not, it should return False. For example, 
list = ['Mary', 'Mary', 'Mary'] #should return True.
#        Extra Challenge: Reverse a String
str1 = "the love is real"
# Write a function called read_backwards that takes a string as 
# an argument and reverses it. For example, the string above 
# should return: "real is love the"

def all_the_same(obj):
    first = obj[0]
    for i in obj:
        if i != first:
            return False
    return True

def read_backwards(str):
    list = str.split()
    list.reverse()
    return ' '.join(list)

print(all_the_same(list))
print(read_backwards(str1))