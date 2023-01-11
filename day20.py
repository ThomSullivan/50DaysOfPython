#       Day 20: Capitalize First Letter
# Write a function called capitalize. This function takes a string 
# as an argument and capitalizes the first letter of each word. For 
# example, ‘i like learning’ becomes ‘I Like Learning’.
# .      Extra Challenge: Reversed List
str1 = 'leArning is hard, bUt if You appLy youRself ' \
  'you can achieVe success'
# You are given a string of words. Some of the words in the string
# contain uppercase letters. Write a code that will return all the 
# words that have an uppercase letter. Your code should return a 
# list of the words. Each word in the list should be reversed. Here 
# is how your output should look:
# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
import re

def capitalizer(str):
    list = str.split(' ')
    return ' '.join([x.capitalize() for x in list])

def reversed_list(str):
    word_list = str.split(' ')
    return [x[::-1] for x in word_list if bool(re.search('([A-Z])', x)) is True]
    
print(capitalizer('i like learning'))
print(reversed_list(str1))