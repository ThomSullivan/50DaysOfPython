#       Day 8: Odd and Even
# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the 
# difference between the largest even number in the list and the 
# smallest odd number in the list. For example, if you pass 
input = [1,2,4,6] 
# as an argument the function should return 6 -1= 5.
#       Extra Challenge: List of Prime Numbers
# Write a function called prime_numbers. This function asks a 
# user to enter a number (integer) as an argument and returns a 
# list of all the prime numbers within its range. For example, if user 
# enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def odd_even(list):
    odds = [x for x in list if x % 2 != 0]
    evens = [x for x in list if x % 2 == 0]
    return max(evens) - max(odds)

print(odd_even(input))

def prime_numbers(int):
    result = []
    for i in range(2, int+1):
        if i <= 3:
            result.append(i)
        elif i % 2 == 0:
            pass
        elif i % 3 == 0:
            pass
        else:
            result.append(i)
    return result

print(prime_numbers(1000))