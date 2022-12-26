#       Day 5: My Discount
# Create a function called my_discount. The function takes no 
# arguments but asks the user to input the price and the 
# discount (percentage) of the product. Once the user inputs the 
# price and discount, it calculates the price after the discount. 
# The function should return the price after the discount. For 
# example, if the user enters 150 as price and 15% as the discount, 
# your function should return 127.5.
#       Extra Challenge: Tuple of Student Sex
# You work for a school and your boss wants to know how many 
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that 
# will count how many males and females are in the list. Here is a 
# list below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should 
# return:
# [(‘Male’,7), (‘female’,6)]

def my_discount():
    price = input('Enter a price:$ ')
    discount = input('Enter a discount rate: ')
    discount = int(discount)
    price = int(price)
    if 100 - discount >= 0 and 100 - discount <= 100:
        discount = 0.01 * (100 - discount)
        total = price * discount
        return print('$' + str(total) +' is your discounted total')
    else:
        return(print('Error: Invalid discount amount'))

my_discount()

def gender_count(list):
    male = 0
    female = 0
    for item in list:
        if item.casefold() == 'male':
            male += 1
        if item.casefold() == 'female':
            female += 1
        else:
            pass
    return [('Male',male),('female',female)]

print(gender_count(students))