###################### Python Comprehensions #################
# Comprehensions provide a concise way to create lists, sets, or dictionaries.
# They consist of brackets containing an expression followed by a for clause.
# Comprehensions help us to write shorter, cleaner code instead of long loops and conditional statements.

## List Comprehension
# Syntax: [expression for item in iterable]
nums = []
for i in range(6):
    nums.append(i)
print(nums)
# Using List Comprehension
nums = [i for i in range(6)]
print(nums)

# List Comprehension with Condition
# Syntax: [expression for item in iterable if condition]
evens = []
for i in range(1,11):
    if i % 2 == 0:
        evens.append(i)
print(evens)

# Using List Comprehension with Condition
evens = [i for i in range(1,11) if i % 2 == 0]
print(evens)

# Transforming Values 
## Squares of numbers
squares = [i*i for i in range(1,6)]
print(squares)

## Uppercase strings

names = ["vali","shaik","python"]
upper_names = [n.upper() for n in names]
print(upper_names)

## Dictionary Comprehension
# Syntax: {key_expression: value_expression for item in iterable}
## Normal Loop
squares = {}
for i in range(1,6):
    squares[i] = i*i
print(squares)

# Using Dictionary Comprehension

squares = {i : i * i for i in range(1,7)}
print(squares)

## Set Comprehension
# A set comprehension creates a set using {} and removes duplicates by default
# Syntax: {expression for item in iterable}
## Normal Loop
unique_squares = set()
for i in range(1,6):
    unique_squares.add(i*i)
print(unique_squares)

# Using Set Comprehension
unique_squares = {i*i for i in range(1,6)}
print(unique_squares)

nums = [1,2,2,3,4,3,6]
unique = {i for i in nums}
print(unique)

# Set Comprehension with Condition
even_unique = {i for i in nums if i % 2 == 0}
print(even_unique)

# {Expression for item in iterable if Condition}


## Generator Expression
# Syntax: (expression for item in iterable)
# Looks like a list comprehension, but uses () and doesn't store anything in memory
gen = (i*i for i in range(1,6))
print(gen)
print(list(gen))

# When to use : large data, memory efficiency

##### When to Use What?
'''
| Use case                 | Choose                   |
| ------------------------ | ------------------------ |
| Need a list you’ll reuse | **List comprehension**   |
| Need unique values       | **Set comprehension**    |
| Key–value mapping        | **Dict comprehension**   |
| Huge data / streaming    | **Generator expression** |
| Complex logic            | **Normal loop**          |

'''

## When to use Comprehensions vs loops
### Use comprehensions when:
#### Logic is simple
#### One operation + optional condition
#### Readability improves

### Use loops when:
#### Logic is complex
#### Multiple operations
#### Nested condition
#### Debugging step-by-step

## One-Line Memory Rules
'''
List → []

Dict → {key: value}

Set → {value}

Generator → ()

Simple logic → comprehension

Complex logic → loop
'''

# Exercise Problems
# Create a list of squares of even numbers from 1 to 10
list1 = [i for i in range(1,11)]
print(list1)

#Create a list of squares of even numbers from 1 to 10
squares = [ i * i  for i in range(1,11) if i % 2 == 0]
print(squares)

# From a list of names, create a dictionary with name as key and length as value.
names = ["Vali","Shaik","Python"]
name_length = {name : len(name) for name in names }
print(name_length)

# Exercise 4
nums = [1,2,3,3,4,5,5,5]
unique_squares = {i * i for i in nums if i % 2 != 0}
print(unique_squares)

# Exercise 5
genr = ( i * i for i in range(1,5))
for value in genr:
    print(value)

# Exercise 6
# Why generator is better than a list for very large data?
## Generator is better than a list because generator doesn't store any data in memmory and it will executed one at a time while list will store all data in memory and it will executed at all
'''
A generator is better for large data because it does NOT store values in memory.
It produces one value at a time ("lazy evaluation"), whereas lists allocate memory for all elements at once.
This makes generators highly memory-efficient for large datasets.
'''