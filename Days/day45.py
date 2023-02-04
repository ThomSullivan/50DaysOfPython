#       Day 45: Words & Special Characters
# Write a function called analyse_string that returns the number of 
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
# and, total characters (all letters and special characters minus 
# whitespaces) in a string. Return everything in a dictionary format:
# {“special character”: “number”, “words”: “number”, “total 
# characters”: “number”}
# Use the string below as an argument:
str = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2". Source Wikipedia'
import string

def analyse_string(str):
    symbols = {x for x in string.punctuation}
    results = {'special characters': 0, 'words':0, 'total characters':0 }
    for char in str:
        if char in symbols:            
            results['special characters'] += 1
        if char != ' ':
            results['total characters'] += 1
    results['words'] = len([ x for x in str.split() if len([y for y in x if y in symbols]) == 0])
    return results
         
print(analyse_string(str))