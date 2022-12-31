#       Day 10: Hide my Password
# Write a function called hide_password that takes no 
# parameters. The function takes an input (a password) from a 
# user and returns a hidden password. For example, if the user 
# enters ‘hello’ as a password the function should return ‘*****’ as 
# a password and tell the user that the password is 5 characters
# long.
#       Extra Challenge: A Thousand Separator
# Your new company has a list of figures saved in a list. The issue 
# is that these numbers have no separator. The numbers are 
# saved in the following format:
input2 = [1000000, 2356989, 2354672, 9878098]
# You have been asked to write a code that will convert each of the 
# numbers in the list into a string. Your code should then add a 
# comma on each number as a thousand separator for 
# readability. When you run your code on the above list, your 
# output should be:
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
# Write a function called convert_numbers that will take one 
# argument, a list of numbers above.
def hide_password(str):
    output = ['*' for x in str]
    output = ''.join(output)
    return '{} user password is {} characters long'.format(output, len(str))

def convert_numbers(list):
    return [f"{x:,d}" for x in list]
    
if __name__ == "__main__":
    input1 = input('Input password: ')
    print(hide_password(input1))
    print(convert_numbers(input2))