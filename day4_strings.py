# 1. What is a String?

## A string is a  sequence of characters inside quotes.
# It can be defined using single quotes(' '), double quotes(" "), or triple quotes (''' ''' or """ """).
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, Python!"
triple_quote_str = '''Hello,
This is a multi-line string.'''

# Python accepts:
## "double quotes"
## 'single quotes'
## """ triple double quotes""" (for multi-line text)
## ''' triple single quotes'''


# 2. Indexing Strings
## Each character in a string has a position (index)

sample_str = "Python"

print(sample_str[0])
print(sample_str[1])
print(sample_str[-1]) # n ( last character )

# Indexing starts from 0, not 1

# String Slicing
## Extracting a part of a string using its index positions

word = "Programming"

print(word[0:5]) # Progr
print(word[:6]) # Progra
print(word[4:]) # ramming
print(word[-3:]) # ing
print(word[:-3]) # Programm


### Format:   string[start : end ]


# 4. String Methods
## Built-in functions that performs specific operations on strings

# .upper() --> Converts string to uppercase
# .lower() --> Converts string to lowercase
# .title() --> Converts first character of each word to uppercase
# .strip() --> Removes whitespace from both ends
# .replace() --> Replaces a substring with another substring (.replace("old","new"))
# .split() --> Splits string into a list based on a delimiter (.split("delimiter"))
# .join() --> Joins elements of a list into a string with a specified delimiter (.join(list))
# .find() --> Finds the index of a substring (.find("substring"))
# .count() --> Counts occurrences of a substring (.count("substring"))
# .startswith() --> Checks if string starts with a specified substring (.startswith("substring"))
# .endswith() --> Checks if string ends with a specified substring (.endswith("substring"))
# .capitalize() --> Capitalizes the first character of the string
# .isdigit() --> Checks if all characters in the string are digits
# .isalpha() --> Checks if all characters in the string are alphabetic
# .isspace() --> Checks if all characters in the string are whitespace
# .format() --> Formats the string using placeholders (example: "Hello, {}".format(name)
# may i know how many methods are there in total?
# there are more than 30 string methods in Python. The ones listed above are some of the most commonly used methods. You can find a complete list in the official Python documentation.

print("String Methods")
text = "  hello python  "
print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())
print(text.replace("python","world"))
print(text.split())
print("-".join(["Hello","World","Python"]))
print(text.find("python"))
print(text.count("o"))
print(text.startswith("  he"))
print(text.endswith("  "))
print(text.capitalize())
print(text.isdigit())
print(text.isalpha())
print(text.isspace())
print("Hello, {}".format("Vali"))


# print("hello python".capitalize())  
# # Output: Hello python

# print("   hello python".capitalize()) 
# # Output:    hello python  (no change, because first character is a space)

#Split Method Simple Explaination
# Example: splitting sentence into characters
# text = "Python"
# print(text.split("t"))


# Output:

# ['Py', 'hon']

"""
| Code              | Behavior                                                |
| ----------------- | ------------------------------------------------------- |
| `text.split()`    | Works → Python splits based on whitespace automatically |
| `text.split(" ")` | Works → splits only where there is a single space `" "` |
| `text.split("")`  | ❌ Error → Python cannot use empty string as separator   |
"""

#5. Concatenation (Joining Strings)

first = "Python"
second="Programming"
result = first + " " + second
print(result)

# Output: Python Programming

#6. Escape Sequences in Strings
## Special characters that are used to represent certain whitespace or non-printable characters within strings.
# Common Escape Sequences:
# \n --> New Line
# \t --> Tab
# \\ --> Backslash
# \' --> Single Quote
# \" --> Double Quote
print("Hello\nWorld")  # New Line
print("Hello\tWorld")  # Tab
print("This is a backslash: \\")  # Backslash
print('He said, \'Hello World!\'')  # Single Quote
print("She said, \"Hello Python!\"")  # Double Quote

#7. String Formatting (f-Strings (Formatted String Literals))
name = "Vali"
age = 22
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Vali and I am 22 years old.

print("########################")
# Exercise 1
first_name = "Shaik"
last_name = "Vali"
print(f"My name is {first_name} {last_name}.")

print("########################")

# Exercise 2

city = " hyderabad "

print("Length of the city before using strip() method: ",len(city))
print("Length of the city after using strip() method: ",len(city.strip())) 
print("UpperCase of City: ",city.upper())
print("Replacing hyd with :",city.replace("hyd","HYD"))

#Length before strip of city which method to use?
#

print("########################")

# Exercise 3

user = input("Enter your city name: ")
print("Length of the user characters: ",len(user))
print("Starting Character of the user sentece: ",user[0])
print("Ending Character of the user sentece: ",user[-1])
print("Title Case of the User Sentence: ",user.title())

print("########################")

# Exercise 4
namee = input("Enter your name: ")
print("Reverse of my name is : ",namee[::-1])

# 🧪 Practice Task (Do Now)

# Create a file day4.py and include:

# ✔ Exercise 1

# Store your:

# first name

# last name

# Then print:

# Your full name is: <first> <last>

# ✔ Exercise 2

# Given:

# city = " hyderabad "


# Print:

# Length before strip

# Length after strip

# Uppercase version

# Replace hyd with HYD

# ✔ Exercise 3

# Ask user:

# Enter a sentence:


# Then output:

# Number of characters

# First character

# Last character

# Sentence in title case

# ✔ Exercise 4 (Bonus 🔥)

# Ask name from the user and print it reversed.

# Hint:

# name[::-1]
