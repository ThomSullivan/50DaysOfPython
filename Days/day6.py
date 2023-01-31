#       Day 6: User Name Generator
# Write a function called user_name that generates a username 
# from the user’s email. The code should ask the user to input an 
# email and the code should return everything before the @ sign 
# as their user name. For example, if someone enters 
user = 'ben@gmail.com'
#  the code should return ben as their user 
# name.
#       Extra Challenge: Zero Both ends
# Write a function called zeroed code that takes a list of numbers 
# as an argument. The code should zero (0) the first and the last 
# number in the list. For example, if the input is 
input = [2, 5, 7, 8, 9]
# your code should return [0, 5, 7, 8, 0].

def user_name(email):
    return email.split('@')[0]

print(user_name(user))

def zeroed(list):
    func_list = list.copy()
    func_list[0] = 0
    func_list[-1] = 0
    return func_list

print(zeroed(input))

