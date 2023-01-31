#       Day 21: List of Tuples
# Write a function called make_tuples that takes two lists, 
# equal lists, and combines them into a list of tuples. For 
# example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
# function should return [(1,5), (2,6), (3,7), (4,8)].
#       Extra Challenge: Even Number or Average
# Write a function called even_or_average that ask a user to 
# input five numbers. Once the user is done, the code should 
# return the largest even number in the inputted numbers. If 
# there is no even number in the list, the code should return the 
# average of all the five numbers.
from statistics import mean

def make_tuples(list1, list2):
    return [(list1[x],list2[x]) for x in range(len(list1))]

def even_or_average(list_of_nums):
    even_list = [x for x in list_of_nums if x % 2 == 0]
    even_list.sort()
    if len(even_list) > 0:
        print('The largest even number is: '+ str(even_list[-1]))
        return even_list[-1]
    print('The average of the odd numbers is '+str(mean(list_of_nums)))
    return mean(list_of_nums)

if __name__ == '__main__':
    a, b = [1,2,3,4], [5,6,7,8]
    print(make_tuples(a,b))
    input_list=[]
    while True:
        num = input('Enter a number: ')
        try:
            num = int(num)
        except:
            print('Invalid input')
            continue
        input_list.append(num)
        if len(input_list) == 5:
            break
    print(input_list)
    even_or_average(input_list)