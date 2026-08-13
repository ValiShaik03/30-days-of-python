# ############## File Handling ##############
# # This day is very important, because files are used everywhere:
# ## logs
# ## data storage
# ## automation
# ## ML datasets
# ## backend systems

# # What is File Handling?
# ## File Handling allows a program to read data from a file or write data into a file
# # Without file handling:
# ## Data is lost when program ends
# # With file handling
# ## Data is stored permanently

# # Types of File Operations
# ## Python mainly supports:
# ### 1. Read
# ### 2. Write
# ### 3. Append
# ### 4. Close

# # Opening a File 
# ## Syntax

# # file = open("Filename.txt","mode")

# # Common modes:
# '''
# | Mode   | Meaning           |
# | ------ | ----------------- |
# | `"r"`  | Read              |
# | `"w"`  | Write (overwrite) |
# | `"a"`  | Append            |
# | `"r+"` | Read + Write      |

# '''
# # Reading a File
# # Example : read()
# file = open("data.txt","r")
# content = file.read()
# print(content)
# print("############")
# file.close()
# # Reads one line only

# # Example: readlines()
# file = open("data.txt","r")
# print(file.readlines())
# print("#######")
# file.close()
# # Reads all lines into a list

# # Writing to a File (w mode)
# ## Important warning
# #### "w" mode deletes existing content

# file = open("data.txt","w")
# file.write("Hello Python\n")
# file.write("Day 15 File Handling")
# file.close()

# # Appending to a File (a mode)
# ## Adds data without deleting existing content
# file = open("data.txt","a")
# file.write("\nAppending new line")
# file.close()

# # with Statement
# ## Automatically closes the file (safe & clean)
# with open ("data.txt","r") as file:
#     content = file.read()
#     print(content)

# # No need to call close()

# # Checking File Exists
# import os
# if os.path.exists("data.txt"):
#     print("File Exists")
# else:
#     print("File not found")
# # Exercise 1
# import os
# if os.path.exists("notes.txt"):
#     print("Notes File Found")
# else:
#     print("File Not Found")
# # Exercise 2
# with open("notes.txt","r") as f:
#     content =f.read()
#     print(content)
# # Exercise 3
# with open("notes.txt","a") as f:
#     f.write("\n File handling is useful")


# ###### print(f.write()) prints character count, not file content.#######

########### File Handling Part-2 ################

# Reading a FIle Line by Line
## Why line by line?
### Saves memory
### Used for logs, large files, datasets

# # Using for loop
# with open("notes.txt","r") as f:
#     for line in f:
#         print(line.strip()) # If we dont use strip it will print one new extra line because in python after each line defaultly developers kept \n at end so to remove it we are using .strip()
# # .strip() removes extra \n

# # Using readlines()
# # with open("notes.txt","r") as f:
# #     lines = f.readlines()
# #     print(lines)
# # Output
# ## ['Line1\n', 'Line2\n', 'Line3\n']
# # Less preferred for large files


# # Writing multiple lines at once(writelines())
# lines = [
#     "Python\n",
#     "File Handling\n",
#     "Day 15\n"
# ] 
# with open("multi.txt","w") as f:
#     f.writelines(lines)

# # writelines() does NOT add newline automatically


# # Handline FileNotFoundError
# # try:
# #     with open("missing.txt","r") as f:
# #         print(f.read())
# # except FileNotFoundError:
# #     print("File does not exist, so please use write operation whenever creating new file that will overwrote and creates a file")

# # Program won't crash
# # User-friendly message


# # Combining os.path.exists() + try-except (BEST PRACTICE)
# import os
# try:
#     if os.path.exists("notes1.txt"):
#         with open("notes1.txt","r") as f:
#             print(f.read())
#     else:
#         print("File not found")
# except Exception as e:
#     print("Unexpected error: ",e)


# # File Pointer(seek() and tell())

# with open("notes.txt","r") as f:
#     print(f.tell()) # current position
#     print(f.read(5)) # read 5 characters
#     print(f.tell()) # new position
#     f.seek(0) # move to start
#     print(f.read(1)) # read 1 character
#     print(f.read())

# # Used in advanced file operations


# # Real-World Mini Program 
# while True:
#     note = input("Enter note (type 'exit' to stop): ")
#     if note.lower() == "exit" or note.upper() == "EXIT":
#         break
#     with open ("notes.txt","a") as f:
#         f.write(note + "\n")
# print("Notes saved successfully")

# Uses append
# Uses loop
# Real-lif use case

# Exercise 1:
# # Read notes.txt line by line and print only lines that contain the word "Python".
with open("notes.txt","r") as f:
    for line in f:
        if "Python" in line:
            print(line.strip())

# Exercise 2

# Write a program that:

# Asks user for name & score

# Appends to results.txt like:
# 
try:
    with open("results.txt","a") as f:
        user = input("Enter your name: ")
        score = input("Enter your score: ")
        result = user + " : " + score + "\n"
        f.write(user + ":" + score + "\n" )
except Exception as e:
    print("Error writing to file:",e)
else:
    print(result)
# 

# Exercise 3:
# Why is "a" mode safer than "w" for logs?
## "a" mode is safer compared to "w" because when we use "a" mode if there is any content in file will not get deleted but in "w" mode existing content will get deleted

import os
if os.path.exists("results.txt"):
    print("Results file found")
else:
    print("not found")

with open("results.txt","r") as f:
    for line in f:
        f.readlines()
        print(line.strip())