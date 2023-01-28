#       Day 38: Guess a Number
# Write a function called guess_a_number. The function 
# should ask a user to guess a randomly generated number. If the 
# user guesses a higher number, the code should tell them that the 
# guess is too high, if the user guesses low, the code should tell 
# them that their guess is too low. The user should get a maximum 
# of three guesses. When the user guesses right, the code should 
# declare them a winner. After three wrong guesses, the code 
# should declare them a loser.
#       Extra Challenge: Find Missing Numbers
numList = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
# Write a function called missing_numbers that takes a list of 
# sequence of numbers and finds the missing numbers in the 
# sequence. The list above should return:
# [4, 8, 10, 13, 16, 29, 30]
from random import randrange
import pyinputplus

def guess_a_number():
    number = randrange(100)
    for i in range(3):
        input = pyinputplus.inputNum('Enter your guess: ')
        if input > number:
            print('Too high')
            continue
        elif input < number:
            print('Too low')
            continue
        else:
            print('You win!')
            return
    print(f'GAMEOVER - {number} was the right answer')
    return

def missing_number(list):
    return [x for x in [*range(min(list), max(list)+1)] if x not in list]

if __name__ == "__main__":
    #guess_a_number()
    print(missing_number(numList))