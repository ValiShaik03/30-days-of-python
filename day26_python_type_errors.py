# 1. What is a TypeError?
## A TypeError happens when Python receives a value of the wrong type for an operation.

# 2. Most Common TypeErrors 
## Example 1: Mixing Types
a = "5"
b = 10
#print(a + b)

# Error:
## TypeError: can only concatenate str (not "int") to str

# FIX
print(int(a) + b)

## Example 2: Wrong argument count
def add(a,b):
    return a + b
# add(5)
# Error:
## TypeError: add() missing 1 required positional argument

# FIX
print(add(5,17))

## Example 3: Calling non-callable
x = 10
# x()
# Error:
## TypeError: 'int' object is not callable

# FIX
## Only call functions
print(x)

## Example 4: Uisng len() incorrectly
### len(5)
# Error:
## TypeError: object of type 'int' has no len()

# FIX
len("5")

# Example 5: Wrong type in list operations
numbers = [1,2,3]
# numbers.append([4,5])
# print(numbers)

# Output :
# [1,2,3,[4,5]]
## Logical TypeError(not syntax error)

# Correct :
numbers.extend([4,5])
print(numbers)

# 4. Fixing TypeErrors WITHOUT try-except
## Instead of this :
try:
    print("5"+10)
except TypeError:
    print("Error")
## Do this:
print(int("5")+10)

# 5. When should we use try-except for TypeError?
## Use it only when:
### Input comes from user
### Data source is unreliable(files,API)

# Example:
try:
    age=int(input("Enter age: "))
except ValueError:
    print("invalid Input")

#### A TypeError occurs when an operation is applied to an object of an inappropriate type,such as adding a string and an integer.
