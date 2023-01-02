#       Day 12: Count the Dots
# Write a function called count_dots. This function takes a 
# string separated by dots as a parameter and counts how many 
# dots are in the string. For example, ‘h.e.l.p.’ should return 4
# dots, and ‘he.lp.’ should return 2 dots.
#       Extra Challenge: Your Age in Minutes
# Write a function called age_in_minutes that tells a user how 
# old they are in minutes. Your code should ask the user to 
# enter their year of birth, and it should return their age in 
# minutes (by subtracting their year of birth to the current year). 
# Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For 
# example, 1930 is a valid year. However, entering any 
# number longer or less than 4 digits long should render 
# input invalid. Notify the user to input a four digits 
# number.
# b. If a user enters a year before 1900, your code should 
# tell the user that input is invalid. If the user enters the 
# year after the current year, the code should tell the user, 
# to input a valid year.
# The code should run until the user inputs a valid year. 
# Your function should return the user's age in minutes. For 
# example, if someone enters 1930, as their year of birth your 
# function should return:
# You are 48,355,200 minutes old.
from datetime import *

def count_dots(str):
    return str.count('.')

def age_in_minutes(year):
    today = date.today()
    if today.year < year:
        return "Invalid input"
    elif year < 1900:
        return "Invalid input"
    else: 
        return ((today.year - year) * 525600)
        
if __name__ == "__main__":
    while True:
        try:
            userYear = int(input("What year were you born? "))
        except:
            print('Invalid input')
            continue
        result = age_in_minutes(userYear)
        if type(result) == int:
            print('You are ' + f"{result:,d}" + ' minutes old.')
            break
        else:
            print(result)
        


