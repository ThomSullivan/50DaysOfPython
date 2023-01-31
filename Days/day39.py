#        Day 39: Password Generator
# Create a function called generate_password that generates any 
# length of password for the user. The password should have a
# random mix of upper letters, lower letters, numbers, and 
# punctuation symbols. The function should ask the user how 
# strong they want the password to be. The user should pick from -
# weak, strong, and very strong. If the user picks weak, the 
# function should generate a 5-character long password. If the user 
# picks strong, generate an 8-character password and if they pick 
# very strong, generate a 12-character password.
import string
import random
import pyinputplus


lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
symbols = string.punctuation
numbers = string.digits

def generate_password(strength):
    password = ''

    match strength:
        case 'weak':
            strength = 5
        case 'strong':
            strength = 8
        case 'very strong':
            strength = 12

    types = ['lower','upper', 'symbol', 'number']
    for i in range(strength):  
        if len(types) == 0:
                types = ['lower','upper', 'symbol', 'number']
        randType = random.choice(types)
        match randType:
            case 'lower':
                password += random.choice(lowerLetters)
                types.remove('lower')
            case 'upper':
                password += random.choice(upperLetters)
                types.remove('upper')
            case 'symbol':
                password += random.choice(symbols)
                types.remove('symbol')
            case 'number':
                password += random.choice(numbers)
                types.remove('number')
    return password

if __name__ == '__main__':
    print('How strong do you want the password to be?')
    strength = pyinputplus.inputMenu(['weak', 'strong', 'very strong'])
    print(f"Your randomly generated password is: {generate_password(strength)}")
     
    
