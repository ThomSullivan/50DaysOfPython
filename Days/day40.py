#   Day 40: Pig Latin
# Write a function called translate that takes the following 
# words and translates them into pig Latin.
a = 'i love python'
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the 
# end. For example, ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move 
# the first letter to the end and add ‘ay’ to the end. For 
# example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay
vowels = ['a','e','o','u','i']

def translate(str):
    words = str.split()
    pigLatin = []
    for word in words:
        if word[0] in vowels:
            pigLatin.append(word +'yay')
        else:
            pigLatin.append(word[1:] + word[0] + 'ay')
    return ' '.join(pigLatin)

print(translate(a))