## Variables
"""
A **Variable** stores data, so python can use it later.
"""

## Rules for Naming Varibales

# 1. A variable can't start with a number
# 2. A variable should not contain any spaces
# 3. Only underscores _ are allowed while naming a variable
# 4. A variable name should be Case - Sensitive (name != Name)
# 5. A variable name should not be any of the Python keywords (like if, else, for, while, etc.)


#Example of invalid variables
# 2name = "X"  # ✖️ starts with a number
# full name = "Y" # ✖️ contains spaces

## Data Types in Python

# Python has several built-in data types. Today we focus on:

# str --> String     "Hello"
# int --> Integer      10
# float ---> Decimal   3.14
# bool ---> Boolean    True,False

name ="vali"
age = 22
height = 5.7
is_Student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_Student))


## Python Built-in Functions
# print() --> Outputs display
# type() --> Check data type
# len() ---> Length of a string/collection
# input() --> Take user input

langauge = "Python"
print(len(langauge))


# 🧑‍💻 🚀 First Interactive Program

name = input("Enter your name:")
print("Hello " + name + "! Welcome to 30 Days of Python Programming")


name = "Vali"
age = 22
print(f"My name is {name} and I am {age} years old")



# Exercise 1

name1 ="vali"
age1=22
food="Chicken Biryani"
city="Cumbum"
print(name1)
print(age1)
print(food)
print(city)

#Exercise 2

print(type(name1))
print(type(age1))
print(type(food))
print(type(city))


#Exercise 3

name2 = input("Enter your name:")
prgmming_lang = input("Enter your favorite programming language")

print(f"Hello " +name1+ "!" + prgmming_lang+" is a great language to learn")

# Exercise 4

print(f"My name is {name1}. I live in {city}.\nI love learning Python and I will master it in 30 days!")