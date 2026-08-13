# Function

## A function is a block of code that runs only when called.
## Example:
def greet():
    print("Hello!")
# To run it we need to call the function by its name:
greet()

# Why do we use functions?
## Avoid repeating code
## Organize code
## Increase readabiity
## Make logic reusable
## Build complex programs easily

'''
1️⃣ Avoid repeating code
❌ Without function (repetition)
print("Hello Shaik")
print("Hello Shaik")
print("Hello Shaik")


If the name changes, you must change it everywhere.

✅ With function (no repetition)
def greet():
    print("Hello Shaik")

greet()
greet()
greet()


Change once → affects everywhere.

👉 Function saves effort and avoids repetition.

2️⃣ Organize code
❌ Without function (messy code)
a = 10
b = 20
print(a + b)

x = 5
y = 3
print(x + y)


Logic is scattered everywhere.

✅ With function (organized)
def add(a, b):
    print(a + b)

add(10, 20)
add(5, 3)


All addition logic is in one place.

👉 Functions keep code clean and organized.

3️⃣ Increase readability
❌ Without function (hard to read)
print((10 * 5) + (20 * 2))


What does this mean? Hard to understand.

✅ With function (easy to read)
def calculate_salary():
    print((10 * 5) + (20 * 2))

calculate_salary()


Now the intention is clear.

👉 Functions make code readable like English.

4️⃣ Make logic reusable
❌ Without function (not reusable)
print(5 * 5)
print(10 * 10)
print(7 * 7)


Same logic, written again and again.

✅ With function (reusable logic)
def square(n):
    return n * n

print(square(5))
print(square(10))
print(square(7))


One function, many uses.

👉 Functions let you reuse logic easily.

5️⃣ Build complex programs easily
❌ Without functions (complex & confusing)
# input
a = int(input())
b = int(input())

# logic
sum = a + b
mul = a * b

# output
print(sum)
print(mul)


As program grows → confusion grows.

✅ With functions (easy & scalable)
def get_input():
    return int(input()), int(input())

def calculate(a, b):
    return a + b, a * b

def display(sum, mul):
    print(sum)
    print(mul)

a, b = get_input()
s, m = calculate(a, b)
display(s, m)


Now the program is structured and easy to expand.

👉 Functions help manage complexity.

🧠 Final One-Line Memory Trick

Functions = small reusable blocks that make code clean, readable, and powerful.
'''

# Defining a function
def function_name():
    pass
function_name()

def welcome():
    print("Welcome to Python Series")
welcome()

# Parameters (Inputs to function)

def greet(name):
    print("Hello",name)
greet("Vali")

#Here name is a "parameter"
# "Vali" is an argument

# Return Statement
# Functions can give back a value

def add(a,b):
    return a+b
result=add(10,5)
print(result)
#If we dont use return and we just use print then it will output and as well as None ,
# but when we use return it will print only our output 
# return sends a value back to the caller

'''
Restaurant analogy 🍽️

print() → waiter announces the dish

return → waiter gives you the dish

Announcing ≠ giving.

If the waiter only announces and doesn’t give food → you receive nothing (None).
'''
'''
PERFECT INTERVIEW ANSWER (Say this confidently):

print() is only for displaying output to the user.
return is used to send a value back to the calling code so it can be reused, stored, or processed further.
A value printed cannot be reused, but a value returned can be assigned to variables, passed to other functions, or used in conditions.
'''

'''
In real applications, functions are rarely written just to print values.
They are written to return data so that other parts of the program, APIs, databases, or models can use that data.
Printing is mainly for debugging or user interaction, while returning is for program logic.
'''

####  **** print is for humans to see, return is for programs to use. **** ####

'''
WHY PRINT IS NOT ENOUGH (CRITICAL POINT)
Print:

Output goes to screen

Value is lost

Cannot be reused

Not suitable for large applications

Return:

Output goes to program

Can be stored

Can be reused

Can be tested

Can be chained

Used in APIs, ML, backend, automation
'''

#### ****** return is a keyword **** ####



## Default Parameters

# Default parameters are used when no argument is passed
# A default parameter is a parameter that already has a value
# If the user does not pass an argument, Python uses the default value
def greet(name="Vali"):
    print("Hello",name) 
greet()
greet("Shaik")

# Default values make functions flexible
# It will prevents errors if input is missing

#### ⚠ Important rule ####
# Default parameters must come after normal paramters

#def test (a=10,b):
    #pass
# This is wrong ❌

def test (a,b=10):
    pass
# This is correct ✔

# Keyword Arguments
## When we pass arguments using the paramter names, not position

# Example:
def info(name,age):
    print(name,age)
# call using keyword arguments
info(age=22,name="vali")

'''
🧠 Why this is useful

* Order does not matter
* Code becomes readable
* Very helpful when many parameters exist
'''

# Variable-Length Arguments(*args)
## Used *args when we don't know how many values will be passed
# Example
def total(*numbers):
    return sum(numbers)
print(total(1,2,3,4))

# Inside the functions, numbers is a tuple
'''
🧠 Why this is useful

Flexible inputs

Used in libraries, frameworks, utilities
'''

# Keyword Variable Arguments (**kwargs)
## Use **kwargs when we dont know how many key-value pairs will be passed

# Example
def profile(**data):
    print(data)

# Call
profile(name ="Vali",age=22,city="Hyderabad")

# Inside the function, data is a dictionary
'''
🧠 Why this is useful

Perfect for user profiles

Used heavily in APIs, configs, JSON data
'''

# Scope(Local vs Global Variables)

## Local Variable

## Defined inside a function and accessible only inside

def test():
    x = 10
    print(x)
#print(x) # Outside Error
test()
# Global Variable

## Defined outside a function

x = 100
def show():
    print(x)
show()

# Modifying global variable

count = 0
def update():
    global count
    count += 1
update()
print(count)


'''
A global variable is defined outside a function and can be accessed inside the function.
To modify it inside a function, the global keyword must be used.
However, using global variables is generally discouraged(
because

* Make code harder to debug

* Can be modified from anywhere

* Cause unexpected bugs); returning values is preferred.
'''
'''
Global variables can be read inside functions, but to modify them you must use the global keyword.
'''

# Lambda Functions (Anonymous Functions)
## A lambda function is a small, one-line function with no name

### Normal Function :
def square(x):
    return x * x
pass

### Lambda Version :
square = lambda x: x * x
print(square(5))

'''
🧠 Why lambda is used

Short operations

Cleaner code

Used in map, filter, sort

⚠ Lambda is for simple logic only.
'''

# Nested Functions

## A function defined inside another function

## Example :
def outer():
    def inner():
        print("Inner Function Running!!!")
    inner()
outer()

'''
🧠 Why this is useful

Encapsulation

Helper logic

Used in decorators (advanced Python)
'''

#### Exercise Problems ####

# Exercise 1:
'''
* Write a function say_hello() that prints:

Output: Hello, welcome to Python!


Call the function 3 times.
'''

def say_hello():
    print("Hello, Welcome to Python!")
say_hello()
say_hello()
say_hello()

# Exercise 2:
'''
Write a function display_square() that prints the square of 5.

Call the function once.
'''

def display_square(n):
    print(n*n)
display_square(5)

# Exercise 3:
'''
Write a function square(n) that:

  * takes one number as parameter

  * prints its square

Call it with:

4

7
'''

def square(n):
    return n * n
print(square(4))
print(square(7))

# Exercise 4:
'''
Write a function add(a, b) that:

returns the sum of two numbers

Store the returned value in a variable and print it.
'''

def add(a,b):
    return a + b
c = add(5,10)
print(c)


# Exercise 5:
'''
Write a function greet(name="Guest") that prints:

Hello <name>


Call it:

without argument

with your name
'''

def greet(name = "Guest"):
    print("Hello",name)
greet()
greet("Vali")


# Exercise 6:
'''
Write a function student_info(name, age, city).

Call the function using keyword arguments, changing the order.
'''

def student_info(name,age,city):
    print(name,age,city)
student_info(age=22,city="Cumbum",name="Vali")

# Exercise 7:
'''
Write a function total_marks(*marks) that:

  * returns the sum of all marks

Call it with:

10, 20, 30, 40
'''
def total_marks(*marks):
    return sum(marks)
print(total_marks(10,20,30,40))

# Exercise 8:

'''
Write a function profile(**details) that prints:

   key : value

for all items.

Call it with:

name="Vali", age=22, course="Python"
'''

def profile(**details):
    for key,value in details.items():
        print(key,":",value)
profile(name="vali",age=22,course="Python")

# Exercise 9:
'''
Create a global variable:

count = 0


Write a function increment() that:

increases count by 1 using global

call the function 3 times

print final value of count
'''

count = 0
def increment():
    global count
    count += 1
increment()
increment()
increment()
print(count)

# Exercise 10:
'''
Write a lambda function that:

   takes one number

   returns its cube

Call it with 3.
'''

cube = lambda x : x ** 3
print(cube(3))

# Exercise 11:
'''
Write a function calculator(a, b) that returns:

   sum
   
   difference

   multiplication

Store returned values and print them.
'''

def calculator(a,b):
    c = a + b
    d = a - b
    e = a * b
    return c,d,e
g,h,i=calculator(5,2)
print(g)
print(h)
print(i)

# Exercise 12:
'''
Write a function is_even(n) that:

returns True if number is even

returns False otherwise

Use the function inside an if condition.
'''

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
result = is_even(3)
print(result)

# Exercise 13:
'''
Write a function find_max(a, b, c) that:

   returns the largest number

Do NOT use max().
'''

def find_max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c
d = find_max(3,4,5)
print(d)

# Exercise 14:
'''
Write a function power(base, exp=2) that:

    returns base raised to exp

Call it:

   with one argument

   with two arguments

'''

def power(base,exp=2):
    return base ** exp
power(2)
power(3,4)


# Exercise 15:
'''
Write a function outer() that:

  defines an inner function inner()

  inner() prints "Inside inner"

  outer() calls inner()

Call outer().

'''
def outer():
    def inner():
        print("Inside Inner")
    inner()
outer()