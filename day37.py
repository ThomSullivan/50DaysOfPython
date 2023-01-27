#       Day 37: Count the Vowels
# Create a function called count_the_vowels. The function 
# takes one argument, a string, and returns the number of vowels
# in the string. For example, ‘hello’ should return 2 vowels. If a 
# vowel appears in a string more than once it should be counted 
# as one. For example, ‘saas’ should return 1 vowel. Your code 
# should count lowercase and uppercase vowels

vowels = ['a', 'e', 'o', 'u', 'i']

def count_the_vowels(str):
    foundVowels = set()
    for letter in str.lower():
        if letter not in vowels:
            continue
        foundVowels.add(letter)
    return len(foundVowels)

print(count_the_vowels('numpy'))
    