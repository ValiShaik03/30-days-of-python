##### Functions Inside Functions
## Python allows a function to be defined inside another function.
def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    inner()
outer()

##### What is a Closure?
## A closure happens when an inner function remembers and uses a variable from the outer function even after the outer function has finished executing.

def greet(name):
    def message():
        print("Hello", name)
    return message
g = greet("Vali")
g()

def remember_name(name):
    def show():
        print("You are", name)
    return show

user1 = remember_name("Vali")
user2 = remember_name("Shaik")

user1()
user2()

# WITHOUT closure
def greet(name):
    return name
x = greet("Vali")
print(x)

def greet(name):
    def message():
        print("Hello",name)
    return message
x = greet("Vali")
x()

def outer():
    x = 10
    def inner():
        print(x)
    return inner
o = outer()
o()


def outer(x):
    def inner(y):
        return x + y
    return inner

test = outer(100)
print(test.__closure__)  # shows saved data

def outer(x):
    print("Outer started")
    def inner(y):
        print("Inner running")
        return x + y
    print("Outer finishing...")
    return inner

add_10 = outer(10)
print("Now outer is gone, but closure still works!")
print(add_10(7))   # calls inner after outer is gone


def outer(x):
    x = 10
    def inner():
        print(x)
    return inner
v = outer(10)
v()

### In my own words
'''
Closure means a function keeps memory of variable of another function after outer function has stopped its execution it still uses a outer variable here in this program we have defined two fuctions 
outer() and inner() and defined one variable x=10 in outer() fuction and in inner function we are printing the outer function variable and returning inner after when we return inner outer function 
has stopped its execution but it will still print the value of outer() function and we have used v variable to call the outer() function and when we call the inner function with outer() object we 
can access the outer variable 
 def outer(x):
    x = 10
    def inner():
        print(x)
    return inner
v = outer(10)
v()
'''

'''
Closure lets inner function keep memory of variables

Even after the outer function finishes execution

We return inner(), store it in a variable like v

Calling v() still prints the outer variable

Because inner remembers outer environment
'''

################ Decorator ##################

# A decorator is just closure + a wrapper
# It allows us to add extra behaviour to a function without changing its code

'''
Normal function = tea
Decorator adds + milk + sugar + flavor without touching original tea

'''
### Without Decorator
def check(func):
    def wrapper():
        print("Checking....")
        func()
    return wrapper
def hello():
    print("Hi")
hello = check(hello) # hello = check(hello) means the original hello function is replaced by the decorated version, while keeping the same name for easier usage.
hello()

#### OWN EXPLAINATION
'''
I am explaining it to you so please clarify if there are any mistakes 
hello=check(hello) is same because when we use same then it will use 
decoratored version first then func() uses a pointer so it come backs 
to original function then print the hello message and how it is printing 
the hello message is in original function after hello=check(hello), 
we called hello() by using this func() refers to it and printed 
hello message and hello=check(hello) is used for to redirect to 
decorated version first then it will comes back to original function 
with the help of func() reference and prints hello message if we dont 
pass same name then it will not print the decorated version
'''

### With Decorator
def check(func):
    def wrapper():
        print("Checking...")
        func()
    return wrapper
@check
def hello():
    print("hi")

hello()

### Decorator With Arguments

## *args are postional arguments for example if we greet(name,age) whenever we are printing it we must need to give in same order ("Vali",22)
# otherwise it will break, it follows order and
## **kwargs are keyword arguments means they have key and value at defining the function like greet(name="vali",age=22)
# so whenever we are printing or calling it if we give (22,"Vali") it still takes and doesn't break because we have passed both key and value at defining the function

### Why do we need *args and **kwargs?
## Because different functions accept different number of inputs
# Example:
'''
def hello():                  # 0 arguments
def greet(name):              # 1 argument
def add(a, b):                # 2 arguments
def details(name, age, city): # 3 arguments

'''
# A decorator must work for ALL of them
# So instead of writing different wrappers like:
'''
def wrapper():
def wrapper(name):
def wrapper(a, b):
def wrapper(name, age, city):

'''
# This is impossible and messy
# So we are using only one function that can take any number of arguments and only one wrapper function that can accepts any number of arguments in any order like :
'''
def wrapper(*args, **kwargs):
    func(*args, **kwargs)

'''
def check(func):
    def wrapper(*args,**kwargs):
        print("Before function runs")
        result = func(*args,**kwargs)
        return result
    return wrapper
@check
def greet(name):
    print("Hello",name)
greet("Vali")

def check_age(func):
    def wrapper(age):
        if age < 18:
            print("Underage -- Not allowed")
        else:
            func(age)
    return wrapper
@check_age
def watch_movie(age):
    print("Movie allowed")
watch_movie(17)
watch_movie(20)


###### Decorator Returning Values
# Until now, decorators only printed
# But sometimes the original function returns a result (sum,output,data)
# Then wrapper must return the value too

### Decorator WITHOUT return
def log(func):
    def wrapper(a, b):
        print("Running function...")
        func(a, b)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(3, 5))   # prints → None

# Because wrapper didn't return the result, output becomes None

### Decorator WITH returning value

def log(func):
    def wrapper(a,b):
        print("Running function...")
        result = func(a,b) # call original and store result
        return result # return result to caller
    return wrapper
@log
def add(a,b):
    return a + b
print(add(5,3))

# Wrapper returned the value
# add() output is preserved

def twice(func):
    def wrapper():
        result = func() # get returned value
        return result * 2 # modify and return
    return wrapper
@twice
def number():
    return 10
print(number())

### If wrapper does NOT return a value then decorated function will return NONE, even if the original function had a return

####### Multiple Decorators
## Multiple Decorators mean stacking more than one decorator on the same function

def star(func):
    def wrapper():
        print("********")
        func()
        print("*******")
    return wrapper
def smile(func):
    def wrapper():
        print("😊😊😊😊")
        func()
        print("😊😊😊😊")
    return wrapper
@star
@smile
def hello():
    print("hello")
hello()

## Execution flow
'''
hello = star(smile(hello)
hello()
  |
star.wrapper() -->runs first
  |
prints ***
  |
calls func() --> func = smile.wrapper
  |
smile.wrapper() runs
  |
prints "😊😊😊"
  |
calls func() --> original hello()
  |
original hello() prints "hello"
  |
smile.wrapper prints "😊😊😊"
  |
star.wrapper prints "****"
'''


###### Decorator with Arguments
## Normally, decorators look like this:
@log
def func():
    pass
# But sometimes we want a customizable decorator -- meaning we pass a value to the decorator itself,like:
#@repeat(3)
def greet():
    print("Hello")
# This means:
## Run the function 3 times

# KEY IDEA : 3 Levels of Function:
## A decorator that takes arguments requires three nested functions
# Level 1 -- receives decorator argument
# Level 2 -- receives function
# Level 3 -- wrapper that actually runs

def say(msg): # Level 1 decorator argument
    def decorator(func): # Level 2 original function
        def wrapper(): # Level 3 - executes
            print(msg)
            func()
        return wrapper
    return decorator
@say("Good Morning")
def greet():
    print("Hello")
greet()

# greet = say("Good Morning")(greet)

#### Decorator with arguments = needs three functions so it can accept custom settings before wrapping

def square_output(func):
    def wrapper():
        result = func()
        return result * result
    return wrapper
@square_output
def num():
    return 5
print(num())


##### Chaining Decorators
# It means a decorator RE-uses another decorator
# Or output of one decorator goes into another
## Example
def double(func):
    def wrapper():
        return func() * 2
    return wrapper
@double
@double
def num():
    return 5
print(num())

# Why 20?
'''
num() = double(double(original))
inner double: func() = 5 → returns 10
outer double: func() = 10 → returns 20

'''

def add_one(func):
    def wrapper():
        return func() + 1
    return wrapper
@add_one
@add_one
@add_one
def number():
    return 0
print(number())
'''
Original number()  returns 0
1st decorator → returns 1
2nd decorator → returns 2
3rd decorator → returns 3

'''
def repeat_twice(func):
    def wrapper():
        func()
        func()
    return wrapper
@repeat_twice
def greet():
    print("HI")
greet()

'''
# greet = repeat_twice(greet)

repeat_twice receives func (which is greet)

wrapper() calls func() twice

repeat_twice returns wrapper
'''


'''
Chaining decorators = applying decorators on top of each other → each layer wraps the next → execution multiplies.
'''
hello=repeat_twice(repeat_twice(repeat_twice(hello)))


def uppercase(func):
    def wrapper ():
        result = func().upper()
        return result
    return wrapper
def loud(func):
    def wrapper():
        result = func() + ("!")
        return result
    return wrapper
@uppercase
@loud
def greet():
    return "hello"
print(greet())

def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("call",count)
        return func()
    return wrapper
@count_calls
def hi():
    print("Hi")
hi()
hi()


######### Real-World Decorator Use Cases

# Example 1: Authentication/Login Check

def require_login(func):
    def wrapper(user):
        if user != "admin":
            print("⛔ Access denied")
        else:
            return func(user)
    return wrapper

@require_login
def dashboard(user):
    print("Welcome", user)

dashboard("guest")
dashboard("admin")
# Security added without changing original function

# Example 2: Logging Every Function Call
def log(func):
    def wrapper(*args, **kwargs):
        print("📜 LOG:", func.__name__, "was called")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

print(add(2, 3))

# Example 3: Measure Execution Time (Performance)
import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("⏱ Time:", end - start)
        return result
    return wrapper

@timer
def run():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

run()
# Used in ML training, API calls, expensive operations

# Example 4: Prevent Function from Running Too Often

def allow_once(func):
    called = False
    def wrapper():
        nonlocal called
        if called:
            print("⚠ Function already used once")
        else:
            func()
            called = True
    return wrapper

@allow_once
def vote():
    print("🗳 Vote submitted")

vote()
vote()

# Example 5: Input Validator
def validate_age(func):
    def wrapper(age):
        if age < 18:
            print("❌ Underage")
        else:
            func(age)
    return wrapper

@validate_age
def enter(age):
    print("Welcome inside!")

enter(12)
enter(25)


#################### QUICK CHEAT SHEET ###########################
############################################################
#                🌙 DAY 19 — CLOSURES & DECORATORS
############################################################

# ---------------- 1️⃣ CLOSURES ----------------
"""
Closure = inner function remembers variables from outer function
even after outer function has finished execution.

Why needed?
✔ protect data (encapsulation-like)
✔ create function factories
✔ maintain state without globals
"""

def outer(x):
    def inner():
        print(x)       # remembers x even after outer() ended
    return inner

v = outer(10)
v()   # prints 10   (closure behavior)


# Example: function generator (real world)
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))  # 10


# ---------------- 2️⃣ DECORATORS (Basics) ----------------
"""
Decorator = a function that takes another function,
adds extra behavior, returns new function
WITHOUT modifying original code.
"""

def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@deco
def say():
    print("Hello")

say()     # Before, Hello, After


# ---------------- 3️⃣ RETURNING VALUES IN DECORATOR ----------------
def square_output(func):
    def wrapper():
        result = func()
        return result * result
    return wrapper

@square_output
def num():
    return 5

print(num())   # 25


# ---------------- 4️⃣ DECORATOR WITH ARGUMENTS ----------------
# Use *args & **kwargs so decorator works with ANY function

def log(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


# ---------------- 5️⃣ MULTIPLE DECORATORS (CHAINING) ----------------
"""
@A
@B
def f():
Execution order:  A -> B -> f
Wrapping order:   f = A(B(f))
"""

def A(func):
    def wrapper():
        print("A")
        func()
    return wrapper

def B(func):
    def wrapper():
        print("B")
        func()
    return wrapper

@A
@B
def hello():
    print("Hello")

hello()   # A, B, Hello


# ---------------- 6️⃣ DECORATOR REAL-WORLD USE CASES ----------------

# Authentication
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            func(user)
    return wrapper

@require_admin
def dashboard(user):
    print("Welcome", user)

dashboard("guest")   # Access denied
dashboard("admin")   # Welcome admin


# Logging & performance
import time
def timer(func):
    def wrapper():
        start = time.time()
        r = func()
        print("Time:", time.time() - start)
        return r
    return wrapper


# ---------------- 7️⃣ COUNT CALLS DECORATOR ----------------
def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("call", count)
        return func()
    return wrapper

@count_calls
def hi():
    print("Hi")

hi(); hi(); hi()


# ---------------- 8️⃣ KEY POINTS TO REMEMBER ----------------
"""
✔ Closure → preserves state
✔ Decorator → wraps + modifies behavior
✔ wrapper() replaces original
✔ return wrapper  (MOST important line)
✔ @decorator == function = decorator(function)
✔ Multiple decorators → outermost executes first
✔ *args / **kwargs = supports any arguments
"""

############################################################
# END OF DAY-19 SUMMARY 📌 — Save this for revision
############################################################
############################################################
#                🌙 DAY 19 — CLOSURES & DECORATORS
############################################################

# ---------------- 1️⃣ CLOSURES ----------------
"""
Closure = inner function remembers variables from outer function
even after outer function has finished execution.

Why needed?
✔ protect data (encapsulation-like)
✔ create function factories
✔ maintain state without globals
"""

def outer(x):
    def inner():
        print(x)       # remembers x even after outer() ended
    return inner

v = outer(10)
v()   # prints 10   (closure behavior)


# Example: function generator (real world)
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))  # 10


# ---------------- 2️⃣ DECORATORS (Basics) ----------------
"""
Decorator = a function that takes another function,
adds extra behavior, returns new function
WITHOUT modifying original code.
"""

def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@deco
def say():
    print("Hello")

say()     # Before, Hello, After


# ---------------- 3️⃣ RETURNING VALUES IN DECORATOR ----------------
def square_output(func):
    def wrapper():
        result = func()
        return result * result
    return wrapper

@square_output
def num():
    return 5

print(num())   # 25


# ---------------- 4️⃣ DECORATOR WITH ARGUMENTS ----------------
# Use *args & **kwargs so decorator works with ANY function

def log(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


# ---------------- 5️⃣ MULTIPLE DECORATORS (CHAINING) ----------------
"""
@A
@B
def f():
Execution order:  A -> B -> f
Wrapping order:   f = A(B(f))
"""

def A(func):
    def wrapper():
        print("A")
        func()
    return wrapper

def B(func):
    def wrapper():
        print("B")
        func()
    return wrapper

@A
@B
def hello():
    print("Hello")

hello()   # A, B, Hello


# ---------------- 6️⃣ DECORATOR REAL-WORLD USE CASES ----------------

# Authentication
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            func(user)
    return wrapper

@require_admin
def dashboard(user):
    print("Welcome", user)

dashboard("guest")   # Access denied
dashboard("admin")   # Welcome admin


# Logging & performance
import time
def timer(func):
    def wrapper():
        start = time.time()
        r = func()
        print("Time:", time.time() - start)
        return r
    return wrapper


# ---------------- 7️⃣ COUNT CALLS DECORATOR ----------------
def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("call", count)
        return func()
    return wrapper

@count_calls
def hi():
    print("Hi")

hi(); hi(); hi()


# ---------------- 8️⃣ KEY POINTS TO REMEMBER ----------------
"""
✔ Closure → preserves state
✔ Decorator → wraps + modifies behavior
✔ wrapper() replaces original
✔ return wrapper  (MOST important line)
✔ @decorator == function = decorator(function)
✔ Multiple decorators → outermost executes first
✔ *args / **kwargs = supports any arguments
"""

############################################################
# END OF DAY-19 SUMMARY 📌 — Save this for revision
############################################################
'''
############################################################
#                🌙 DAY 19 — CLOSURES & DECORATORS
############################################################

# ---------------- 1️⃣ CLOSURES ----------------
"""
Closure = inner function remembers variables from outer function
even after outer function has finished execution.

Why needed?
✔ protect data (encapsulation-like)
✔ create function factories
✔ maintain state without globals
"""

def outer(x):
    def inner():
        print(x)       # remembers x even after outer() ended
    return inner

v = outer(10)
v()   # prints 10   (closure behavior)


# Example: function generator (real world)
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))  # 10


# ---------------- 2️⃣ DECORATORS (Basics) ----------------
"""
Decorator = a function that takes another function,
adds extra behavior, returns new function
WITHOUT modifying original code.
"""

def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@deco
def say():
    print("Hello")

say()     # Before, Hello, After


# ---------------- 3️⃣ RETURNING VALUES IN DECORATOR ----------------
def square_output(func):
    def wrapper():
        result = func()
        return result * result
    return wrapper

@square_output
def num():
    return 5

print(num())   # 25


# ---------------- 4️⃣ DECORATOR WITH ARGUMENTS ----------------
# Use *args & **kwargs so decorator works with ANY function

def log(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


# ---------------- 5️⃣ MULTIPLE DECORATORS (CHAINING) ----------------
"""
@A
@B
def f():
Execution order:  A -> B -> f
Wrapping order:   f = A(B(f))
"""

def A(func):
    def wrapper():
        print("A")
        func()
    return wrapper

def B(func):
    def wrapper():
        print("B")
        func()
    return wrapper

@A
@B
def hello():
    print("Hello")

hello()   # A, B, Hello


# ---------------- 6️⃣ DECORATOR REAL-WORLD USE CASES ----------------

# Authentication
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
        else:
            func(user)
    return wrapper

@require_admin
def dashboard(user):
    print("Welcome", user)

dashboard("guest")   # Access denied
dashboard("admin")   # Welcome admin


# Logging & performance
import time
def timer(func):
    def wrapper():
        start = time.time()
        r = func()
        print("Time:", time.time() - start)
        return r
    return wrapper


# ---------------- 7️⃣ COUNT CALLS DECORATOR ----------------
def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("call", count)
        return func()
    return wrapper

@count_calls
def hi():
    print("Hi")

hi(); hi(); hi()


# ---------------- 8️⃣ KEY POINTS TO REMEMBER ----------------
"""
✔ Closure → preserves state
✔ Decorator → wraps + modifies behavior
✔ wrapper() replaces original
✔ return wrapper  (MOST important line)
✔ @decorator == function = decorator(function)
✔ Multiple decorators → outermost executes first
✔ *args / **kwargs = supports any arguments
"""

Closure = remembers values
Decorator = adds behavior

############################################################
# END OF DAY-19 SUMMARY 📌 — Save this for revision
############################################################

'''