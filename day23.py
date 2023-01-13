#        Day 23: Simple Calculator
# Create a simple calculator. The calculator should be able to perform 
# basic math operations, add, subtract, divide and multiply. The 
# calculator should take input from users. The calculator should be 
# able to handle ZeroDivisionError, NameError, and 
# ValueError.
#        Extra Challenge: Multiply Words
# s = "love live and laugh"
# Write a function called multiply_words that takes a string as an 
# argument and multiplies the length of each word in the string by 
# the length of other words in the string. For example, the string 
# above should return 240 - love (4) live (4) and (3) laugh (5). 
# However, your function should only multiply words will all 
# lowercase letters. If a word has one upper case letter, it should be 
# ignored. For example, the following string:
# s = "Hate war love Peace" should return 12 – war (3) love (4). 
# Hate and Peace will be ignored because they have at least one 
# uppercase letter.

import operator
from functools import reduce

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
}
s1 = "love live and laugh"
s2 = "Hate war love Peace"

def calculate(oper, num1, num2):
    value = ops[oper](num1,  num2)
    return value

def multiply_words(str):
    nums = [len(x) for x in str.split() if x.islower() == True]
    return reduce((lambda x, y: x * y), nums)


if __name__ == '__main__':
    print(multiply_words(s1))
    print(multiply_words(s2))
    while True:
        num1 = input('Enter first number: ')
        try:
            num1 = int(num1)
        except ValueError:
            print('That is not a number')
            continue
        oper = input('choose an operator (+,-,*,/)')
        if oper not in ops.keys():
            print('That is not a valid operator')
            continue
        num2 = input('Enter scond number: ')
        try:
            num2 = int(num2)
        except ValueError:
            print('That is not a number')
            continue
        print(calculate(oper,num1, num2))
        break