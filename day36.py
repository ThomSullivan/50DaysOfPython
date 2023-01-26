# Day 36: Count String
# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element 
# appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(str):
    count = {}
    for char in str:
        if char not in count.keys():
            count[char] = 0
        count[char] += 1
    return count

print(count('hello'))
