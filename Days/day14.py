#       Day 14: Flatten the List
# Write a function called flat_list that takes one argument, a 
# nested list. The function converts the nested list into a one dimension list. For 
example = [[2,4,5,6]] #should return [2,4,5,6].
#        Extra Challenge: Teacher’s Salary
# A school has asked you to write a program that will calculate 
# teachers' salaries. The program should ask the user to enter the 
# teacher’s name, the number of periods taught in a month, 
# and the rate per period. The monthly salary is calculated by 
# multiplying the number of periods by the monthly rate. 
# The current monthly rate per period is $20. If a teacher has 
# more than 100 periods in a month, everything above 100 is 
# overtime. Overtime is $25 per period. For example, if a teacher 
# has taught 105 periods, their monthly gross salary should be 
# 2,125. Write a function called your_salary that calculates a 
# teacher’s gross salary. The function should return the 
# teacher’s name, periods taught, and gross salary. Here is 
# how you should format your output:
# Teacher: John Kelly, 
# Periods: 105 
# Gross salary:2,125

def flat_list(list):
    return_value = list.copy()
    return_value = return_value[0]
    return return_value

def your_salary(periods):
    gross = 0
    if periods > 100:
        gross += 5 * (periods-100)
    gross += 20 * periods
    return gross
    
if __name__ == '__main__':
    flat_list(example)
    name = input('Enter name: ')
    while True:
        periods = input('Enter periods taught: ')
        try:
            periods = int(periods)
        except:
            print('Enter a valid number')
            continue
        if periods < 0:
            print('Enter a valid number')
            continue
        print('Teacher: {},\nPeriods: {},\nGross salary: {}'.format(name,periods,your_salary(periods)))
        break
