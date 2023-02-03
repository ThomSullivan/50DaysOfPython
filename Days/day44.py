#       Day 44: Save Emails
# Create a function called save_emails. This function takes no 
# arguments but asks the user to input email, and it saves the 
# emails in a CSV file. The user can input as many emails as they 
# want. Once they hit ‘done’ the function saves the emails and 
# closes the file. Create another function called open_emails. 
# This function opens and reads the content of the CSV file. Each 
# email must be in its line. Here is an example of how the emails 
# must be saved:
# jj@gmail.com
# kate@yahoo.com
# and not like this:
# jj@gmail.comkate@yahoo.com

import pyinputplus
import csv

def save_emails(filePath):
    with open(filePath,'w',newline='') as csvfile:
        emailWriter = csv.writer(csvfile)
        while True:
            email = pyinputplus.inputEmail(prompt="Enter an email to save(leave blank to quit): ", blank=True)
            if len(email) == 0:
                print('All done')
                break
            emailWriter.writerow([email])
            print(f'{email} added to the file')
        

def open_emails(filePath):
    with open(filePath, 'r') as csvfile:
        val = csvfile.read()
    print(val)
    return val

if __name__ == "__main__":
    filePath = 'csvFiles/day44Data.csv'
    save_emails(filePath)
    open_emails(filePath)
