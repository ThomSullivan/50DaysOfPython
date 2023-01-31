#       Day 17: User Name Generator
# Write a function called user_name, that creates a username 
# for the user. The function should ask a user to input their name. 
# The function should then reverse the name and attach a 
# randomly issued number between 0 – 9 at the end of the name. 
# The function should return the username.
#       Extra Challenge: Sort by Length
names = ['Peter','Jon','','Andrew','zuul']
# Write a function called sort_length that takes a list of strings
# as an argument, and sorts the strings in ascending order 
# according to their length. For example, the list above should 
# return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions
from random import randint

def random_user_name(string):
    num =randint(0, 9) 
    return string[::-1].lower() + str(num)

def sort_length(list):
    new_list = list.copy()
    for j in range(len(list)):
        for i in range(len(list)-1):
            if len(new_list[i]) > len(new_list[i+1]):
                new_list.append(new_list[i])
                new_list.remove(new_list[i])
    return new_list






if __name__ == "__main__":
    input = input('Enter your name to recieve a username: ')
    print('Your user name is: ' +random_user_name(input))

    print(sort_length(names))