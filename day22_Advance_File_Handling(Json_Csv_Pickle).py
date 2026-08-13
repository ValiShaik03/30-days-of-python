################### Advanced File Handling (JSON . CSV . PICKLE)
# 1. JSON(JavaScript Object Notation)
## What is JSON ?
### Text-based format
### Stores dicts, lists, strings, numbers, booleans
### Widely used in APIs & configs

# Why JSON when we are having Dictionary because JSON is also used to store in a dictionary way???
## Python Dictionary
'''
This dictionary:

Lives only in RAM

Exists only while the program is running

Is Python-specific

Disappears when the program ends ❌

So:
If we close our program --> dictionary is gone

'''
## JSON
'''
This JSON:

* Lives in a file

* Is saved on disk

* Can be shared between:

  * Python

  * Java

  * JavaScript

  * C++

  * APIs

  * Exists even after program ends ✅

So:

If we close our program → JSON file still exists.
'''

'''
Dictionary = Python’s internal brain memory
JSON = Universal language for storing & sharing data

'''
# Example JSON file(data.json)
# {
#     "name":"Vali",
#     "age": 22,
#     "skills":["Python","AI"]    
# }

# Read JSON
import json
with open("data.json","r") as f:
    data = json.load(f)
print(data["name"])
print(data["skills"])

# What happens internally?
## Python opens data.json
## Reads the text
## Converts it into a Python dictionary
## Stores it in variable data
# Write JSON
import json
user = {
    "name":"Shaik",
    "age":25,
    "skills":["ML","Data"]
}
with open("user.json","w") as f:
    json.dump(user, f, indent = 4)

import json
user1 = {
    "name":"valishaik",
    "education":"B. Tech",
    "Job":"Searching..."
}
with open("user2.json","w") as f:
    json.dump(user1,f,indent=4)

# json.dump() -- Takes a Python dictionary/list and saves it as JSON text into a file
## What happens internally?
# Python takes the dictionary user1
# Converts it into JSON text
# Writes that text into user2.json
# json.dump() = Python --> file 


# 2. CSV (Comma Separated Values)

## It is just a text file that stores data in rows and columns, like a table
### Example(students.csv)
# name,age,marks
# Vali,22,90
# Shaik,25,90

# Why CSV when we already have lists & dictionaries?
## Python list/dict -- where do they live?
students =[
    {"name":"vali","age":22,"marks":90},
    {"name":"Shaik","age":25,"marks":98}
]
# This data:
'''
📌 This data:

Lives only in RAM

Exists only while program runs

Disappears when program stops ❌

Cannot be opened directly in Excel
'''
# CSV -- Where does it live?
# name,age,marks
# Vali,22,90
# Shaik,25,85

## This data:
'''
📌 This data:

Lives in a file on disk

Exists even after program ends ✅

Can be opened in:

Excel

Google Sheets

Python

R

Any data tool

Used heavily in data analysis
'''

## Real-World Use Case
'''
Scenario: Marks system in a college

Teachers enter marks in Excel

File is saved as CSV

Python program reads CSV

Calculates:

Average

Rank

Pass/Fail

Writes result back to CSV

👉 This is why CSV exists.
'''

##### CSV vs JSON
'''
| Feature        | CSV                  | JSON               |
| -------------- | -------------------- | ------------------ |
| Structure      | Table (rows/columns) | Nested (dict/list) |
| Best for       | Tabular data         | Structured data    |
| Excel friendly | ✅ Yes                | ❌ No               |
| API usage      | ❌ Rare               | ✅ Very common      |
| Human readable | Medium               | High               |

'''

# How Python Reads CSV
## Python gives a csv module
### Reads CSV (row by row)
print("###################")
import csv
with open("students.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("##################")
## Better Way : DictReader (Recommended)
import csv
with open("students.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# Now Each Row Becomes A Dictionary
# Column names become keys

# Writing CSV from Python
import csv
data =[
    {"Name":"Ashok","Subject":"Physics","Age":40},
    {"Name":"Aparna","Subject":"C Language","Age":30}
]
with open("teachers.csv","w",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["Name","Subject","Age"])
    writer.writeheader() # Without this line no headings will be appeared in our csv file
    writer.writerows(data) # Without this line no rows like our dat awill not be appeared just headings will be appeared
# Creates a CSV file usable in Excel

## Why newline = "" is important?
### Without newline="" the output is:
'''
Name,Subject,Age

Ashok,Physics,40

Aparna,C Language,30


Here On Windows:
* Without newline="" --> extra blank lines appear
* With it --> clean CSV
'''


# 3. Pickle
## Pickle is used to save Python objects exactly as they are
## And load them back later without losing structure

# Why Pickle when we already have JSON/CSV?
## Because JSON and CSV cannot store everything.
### Example Python objects JSON/CSV CANNOT store easily:
#### Sets
#### Tuples
#### Custom class objects
#### Functions (references)
#### Complex nested objects
## Pickle can store all these easily

# 3.1 Where does a Python object normally live?
data = [1,2,3,{"a":10}]
## This object
### Lives only in RAM
### Disappears when program ends

# 3.2 Pickle -- what does it do?
## Pickle converts a Python object into binary format and saves it to a file
### Later:
#### We can load it
#### And get the exact same Python object back

# 3.3 Pickle Example
## Save (Serialize) 
'''
Serialization in Python is the process of converting a data object 
(like a dictionary, list, or class instance) into a format that can be easily stored or transmitted (e.g., a file or a byte stream), and then reconstructed later
'''
import pickle
data ={
    "name":"vali",
    "age":22,
    "skills":["Python","AI"]
}
with open("data.pkl","wb") as f:
    pickle.dump(data,f)
# wb = write binary
# This craetes a file data.pkl
# Not human readable
# Python readable

## Load (Deserialize)
import pickle
with open("data.pkl","rb") as f:
    loaded_data = pickle.load(f)
print(loaded_data)
# Same dictionary comes back

# 3.4 What exactly is happening?
## Internally:
### Pickle converts Python object --> binary stream
### Saves it
### Loads binary stream --> reconstructs Python object
#### Structure, types, nesting -- everything is stored (preserved)

# 3.5 Real-World Use Case
## Example : Machine Learning Model
def train_model(data):
    pass

import pickle
model = train_model(data)
pickle.dump(model,open("model.pkl","wb"))

# Later
model = pickle.load(open("model.pkl","rb"))
print(model)

import pickle

class DummyModel:
    def predict(self, data):
        return "Prediction successful"

# Save
model = DummyModel()
pickle.dump(model, open("model.pkl","wb"))

# Load
loaded_model = pickle.load(open("model.pkl","rb"))
print(loaded_model.predict("new_data"))


#### Exercises

# Exercise 1:
'''
Task

Create a JSON file profile.json

Store: name, age, skills

Read and print age

'''
import json
profile = {
    "name":"vali",
    "age":22,
    "skills":["Python","MySQL","ML Basics"]
}
with open("profile.json","w") as f:
    json.dump(profile,f,indent = 4)
with open("profile.json","r") as f:
    data = json.load(f)
print("Age:",data["age"])

# Exercise 2
'''
Task:
    * Create marks.csv
    * Print students with marks > 85
'''

import csv
with open("marks.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","marks"])
    writer.writerow(["Vali",90])
    writer.writerow(["Shaik",78])
    writer.writerow(["Shaheen",89])
with open("marks.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["marks"]) > 85:
            print(row["name"],row["marks"])


# Exercise 3:
'''
Task
    * Pickle a dictionary
    * Load and print it
'''

import pickle
info = {"day":22,"topic":"File Handling"}
with open("info.pkl","wb") as f:
    pickle.dump(info,f)
with open("info.pkl","rb") as f:
    data = pickle.load(f)
    print(data)

# Exercise 4:
import pickle
class Session:
    def __init__(self,name):
        self.name = name
    def show(self):
        return f"Session by {self.name}"
s = Session("Vali")
pickle.dump(s,open("session.pkl","wb"))
loaded = pickle.load(open("session.pkl","rb"))
print(loaded.show())


################ DAY 22 CHEAT SHEET #######################
'''
# ==================================================
# DAY 22 — ADVANCED FILE HANDLING
# ==================================================

# -------- JSON --------
import json

# Read JSON
json.load(file)

# Write JSON
json.dump(data, file, indent=4)

# load  -> file  -> python
# dump  -> python -> file

# -------- CSV --------
import csv

# Read CSV
csv.reader(file) 
# When we use csv.reader(file) it will produce output as:
'''
['name', 'age', 'marks']
['Vali', '22', '90']
['Shaik', '25', '90']
'''
# But when we use csv.DictReader(file) it will produce output as:
'''
{'name': 'Vali', 'age': '22', 'marks': '90'} 
{'name': 'Shaik', 'age': '25', 'marks': '90'}
'''
csv.DictReader(file)

# Write CSV
csv.writer(file)
csv.DictWriter(file)

# Always use newline="" while writing CSV (Windows)

# -------- Pickle --------
import pickle

# Save object
pickle.dump(obj, open("file.pkl","wb"))

# Load object
pickle.load(open("file.pkl","rb"))

# ⚠️ Do NOT load pickle from untrusted sources

# -------- When to use --------
# JSON   -> APIs, configs, sharing data
# CSV    -> Tables, Excel, datasets
# Pickle -> Python objects (local only)

'''