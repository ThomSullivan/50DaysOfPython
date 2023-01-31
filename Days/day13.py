#       Day 13: Pay Your Tax
# Write a function called your_vat. The function takes no 
# parameter. The function asks the user to input the price of an 
# item and VAT (vat should be a percentage). The function should 
# return the price of the item plus VAT. If the price is 220 and, 
# VAT is 15% your code should return a vat inclusive price of 253. 
# Make sure that your code can handle ValueError. Ensure the 
# code runs until valid numbers are entered. (hint: Your code 
# should include a while loop).
#       Extra Challenge: Pyramid of Snakes
# Write a function called Python_snakes that takes a number
# as an argument and creates the following shape, using the 
# number’s range: (hint: Use the loops and emoji library. If you 
# pass 7 as argument, your code should print the following:
import emoji

def your_vat(price, vat):
    total = (price + ((vat/100) * price))
    return int(total)

def python_snakes(num):
    k = 0
    for i in range(1, num):
        for space in range(1, (num-i)):
            print(end="  ")
        while k!=(2*i-1):
            print(emoji.emojize(':snake:'), end="")
            k += 1
        k = 0
        print()


if __name__ == '__main__':
    while True:
        price = input('Input item price: ')
        vat = input('Input VAT: ')
        try:
            price, vat = int(price), int(vat)
        except:
            print('ValueError')
            continue
        if price <= 0 or vat <=0 or vat >100:
            print('ValueError')
            continue
        else:
            print('Your VAT inclusive price is $' + str(your_vat(price, vat)))
            break
    python_snakes(7)
