#       Day 42: Spelling Checker
# Write a function called spelling_checker. This code asks the 
# user to input a word and if a user inputs a wrong spelling it 
# should suggest the correct spelling by asking the user if they 
# meant to type that word. If the user says no, it should ask the 
# user to enter the word again. If the user says yes, it should 
# return the correct word. If the word entered by the user is 
# correctly spelled the function should return the correct word.
# Use the module textblob.
#       Extra Challenge: Create an Alarm clock
# Create a function called alarm that sets an alarm clock for the 
# user. The function should ask the user to enter time they want 
# the alarm to go off. The user should enter the hour and 
# minute. The function should then print out the time when the 
# alarm will go off. When its alarm time, the code should let off a 
# sound. Use the winsound module for sound.
from textblob import Word
import pyinputplus
import winsound
import time
import datetime

def spelling_check():
    while True:
        word = Word(pyinputplus.inputStr('Spell a word: ', blockRegexes='0123456789'))
        if word != word.spellcheck()[0][0]:
            response = pyinputplus.inputMenu(['Yes','No'],prompt=f'Did you mean {word.spellcheck()[0][0]}?\n')
            if response != 'Yes':
                continue
        return f'The correct spelling is "{word.spellcheck()[0][0]}"'
def alarm():
    now = datetime.datetime.now()
    input = pyinputplus.inputTime(prompt='Set alarm for what time? ')
    alarmDate = datetime.datetime(now.year, now.month, now.day, input.hour, input.minute)
    if input < now.time():
        alarmDate += datetime.timedelta(days=1)
    difference = alarmDate - now
    print(f'Alarm will sound at {alarmDate}')
    time.sleep(round(difference.total_seconds()))
    print('ALARM')
    winsound.PlaySound('SystemDanger', winsound.SND_ALIAS)
if __name__ == '__main__':
    print(spelling_check())
    alarm()
    
    
    