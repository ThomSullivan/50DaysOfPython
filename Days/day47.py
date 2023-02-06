#       Day 47: Save a JSON
# Write a function called save_json. This function takes a 
# dictionary below as an argument and saves it on a file in JSON 
# format.
# Write another function called read_json that opens the file 
# that you just saved and reads its content.
import json

names = {'name': 'Carol','sex': 'female','age': 55}
def save_json(path):
    jsonNames = json.dumps(names, indent=3)
    with open(path, 'w') as jFile:
        jFile.write(jsonNames)

def read_json(path):
    with open(path, 'r') as jFile:
        jsonObj = jFile.read()
    
    print(jsonObj)



path = 'csvFiles/day47Data.json'
save_json(path)
read_json(path)