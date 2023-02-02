#        Day 43: Student Marks
# Write a function called student_marks that records marks 
# achieved by students in a test. The function should ask the user 
# to input the name of the student and then ask the user to input 
# the marks achieved by the student. The information should be 
# stored in a dictionary. The name is the key and the marks is the 
# value. When the user enters done, the function should return a 
# dictionary of names and values entered.
import pyinputplus

def student_marks():
    print('Enter student name and marks - enter no name to quit')
    marks = {}
    while True:
        name = pyinputplus.inputStr('Enter student name: ', blank=True, blockRegexes='0123456789')
        if len(name) == 0:
            break
        grade = pyinputplus.inputInt(min=0, max=100, prompt='Enter student grade: ')
        marks[name] = grade
    return marks
if __name__ == "__main__":
    print(student_marks())