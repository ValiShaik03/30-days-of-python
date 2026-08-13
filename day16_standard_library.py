############ Python Standard Library ############
# The Pyhton Standard Library is a collection of modules and packages included with Python.
# It provides pre-written code to perform common tasks, saving developers timeand effort.
# These modules are used everywhere: scripts,automation,backend,ML pipelines,APIs,etc.

# os Module - Working with Operating System & Filesystem
# ? Why os?
# To interact with:
## Files
## Folders
## Paths
## Environment Variables

#### Get current working directory
import os
print(os.getcwd())

#### List files & folders
import os
print(os.listdir())

print(os.listdir("C:/")) # list files in C drive

## Create a folder
# import os
# os.mkdir("new_folder") # Creates only if it doesn't exist

## Create folders recursively
# import os
# os.makedirs("project1/data/logs") # creates all intermediate folders

## Check file/folder exists
import os
print(os.path.exists("notes.txt")) # True if exists, else False

print(os.path.isfile("notes.txt"))
print(os.path.isdir("project"))

## Delete file / folder
#os.remove("results.txt") # delete file
#os.rmdir("new_folder") 


# 2. sys Module - Pyhton Runtime Information
# ? Why sys ?
# To interact with:
## Python interpreter # interpreter means jo chalata hai python code ko
## command-line arguments
## exit programs

# Python Version
import sys
print(sys.version) # prints version of python

# Command-line arguments
# import sys
# print(sys.argv) # prints list of command line arguments

# Means if we run this file as : python day16_standard_library.py arg1 arg2 then output will be : ['day16_standard_library.py', 'arg1', 'arg2'] 
# Use of sys.argv : Used in scripts to accept user inputs from command line means we can pass inputs while running the script


# Exit program manually
# import sys
# sys.exit("Stopping program")
# print("This will not be printed")
# The above line will stop the program and print "Stopping program"
# Used to terminate program based on conditions or errors

# 3. datetime Module - Working with Dates & Times
# ? Why datetime?
# Used for:
## logs means recording events with date and time
## timestamps means marking events with date and time
## scheduling tasks
## date tracking

# Current date & time
from datetime import datetime
now = datetime.now()
print("Current date & time:",now)

# Only date & time
print(now.date())
print(now.time())

# Custom format 
print(now.strftime("%d-%m-%y %H:%M:%S"))

'''
Common formats:

%d → day

%m → month

%Y → year

%H → hour

%M → minute

%S → second
'''

# Real-World Mini Program
## Logging system with timestamp
from datetime import datetime
msg = input("Enter log message: ")
with open("app.log","a") as f:
    time = datetime.now().strftime("%d-%m%y %H:%M:%S")
    f.write(f"[{time}]{msg}\n")
print("Log saved")

# Output
# Enter log message : Application started
# Log saved
# app.log content :
# [15-06-24 10:30:45]Application started


#### 🎯 Memory Rules 
'''
os → filesystem

sys → interpreter & args

datetime → date & time

strftime() → format time

sys.argv → command-line inputs
'''

# Exercise Problems
# Exercise 1
# Print all files in current directory
import os
print(os.listdir())

# Exercise 2
'''
Print:

Python version

Script name only (from sys.argv)
'''
import sys
print("Python Version: ",sys.version)
print("Script Name: ",sys.argv[0]) # script name is always the first argument

# Exercise 3
# Print current date in DD/MM/YYYY format
from datetime import datetime
now = datetime.now()
print(now.strftime("%d/%m/%Y"))

# import sys
# print(sys.argv)
# print("Script name:", sys.argv[0])
# print("First argument:", sys.argv[1])
# print("Second argument:", sys.argv[2])

# Why is Script Name Included?
# Because when we run a script, the first argument is always the script name itself. This allows the script to know its own name and can be useful for logging or displaying usage information.

# sys.argv is a list in Python --> index 0 = script name --> index 1 + = arguments

# import sys
# print("Script Name: ",sys.argv[0])
# print("First Number: ",sys.argv[1])
# print("Second Number: ",sys.argv[2])
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# print("Sum is :",num1 + num2)

'''
Write a program that:

Takes one name from command line

Prints a greeting

If name is missing, print an error message (no crash)
'''
import sys
if len(sys.argv) < 2:
    print("Error: Name argument is missing")
else:
    name = sys.argv[1]
    print("Hello " + name)


'''
while running this argv exercise program 
i got one clarity that we need a separate file for each argv 
because for each program there are different arguments
'''
## Answer
'''
💯 Excellent clarity — and you are absolutely RIGHT.

sys.argv belongs to a program, not to Python globally.

Each Python file is a separate program

Each program expects its own arguments

Mixing multiple argv logics in one file creates confusion

One script = one responsibility = one argument pattern
'''