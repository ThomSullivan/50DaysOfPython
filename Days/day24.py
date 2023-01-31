#       Day 24: Average Calories
# Create a function called average_calories that calculates the 
# average calories intake of a user. The function should ask the user 
# to input their calories intake for any number of days and once they 
# hit ‘done’ it should calculate and return the average intake.
#       Extra Challenge: Create a Nested List
# Write a function called nested_lists that takes any number of 
# lists and creates a 2-dimensional nested list of lists. For example,
# if you pass the following lists as arguments: [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5].
# Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]

a, b, c = [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]

def average_calories(cals, days):
    return (int(cals)/int(days))

def nested_lists(*args):
    return [x for x in args]

if __name__ == '__main__':
    while True:
        cals = input('Enter number of calories: ')
        try:
            int(cals)
        except:
            print('invalid input')
            continue
        days = input('Enter days over which calories were consumed: ')
        try:
            int(days)
        except:
            print('invalid input')
            continue
        print('You consumed an average of {} calories over {} days'.format(average_calories(cals, days), days))
        break
nested_lists(a,b,c)


