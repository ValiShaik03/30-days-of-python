# Object Oriented Programming

# The big problem OOP solves(why OOP exists)
## Before OOP, we write code like this:
name = "Vali"
age = 22
marks = 85

def display_student():
    print(name, age, marks)

# Now imagine:
### 100 students
### 100 names
### 100 ages
### 100 functions

### ❌ This becomes messy and unmanageable

## OOP groups related data and behaviour together


#### WITH OOP ####
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(self.name,self.age,self.marks)

s1 = Student("Vali",22,85)
s1.display()

# What happened here?
## Data (stored together)
### name
### age
### marks

# Behavior (stored together)
### display()

#### Both belong to ONE student object

'''
2️⃣ Core idea of OOP (ONE sentence)

OOP = Data + Functions kept together

This “together” unit is called an object.
'''

'''
3️⃣ Real-life analogy
Think about a Car

A car has:

brand

model

color

A car can:

start()

stop()

drive()

You don’t write:

brand separately

start() separately

👉 Everything belongs to the same car.

That “car” is an object.
'''

# 4️⃣ What is a CLASS? (Blueprint)
### A class is a blueprint/design/template
#### It tells Python:
## What data an object will have
## What actions it can perform

# Example(just a design):
class Student:
    pass

#⚠️ This does not create a student
# It only describes how a student should look

# 5️⃣ What is an OBJECT? (Real thing)
### An object is created from a class
s1 = Student()
# Here:
### Student ----> blueprint
### s1 ---------> real object

#### We can create many objects from one class:
s2=Student()
s3=Student()

'''
6️⃣ Class vs Object (CLEAR difference)
Class	                Object
Blueprint	           Real thing
No memory for data	   Stores real data
Design	               Instance

🧠 Class = idea, Object = reality
'''

# 7️⃣ Adding DATA to a class (Attributes)

class Student:
    name = "Vali"
    age = 22
# Now:
s1 = Student()
print(s1.name)
print(s1.age)

# Output:
## Vali
## 22

#⚠️ These are class variables (same for all objects).

# 8️⃣ What is a METHOD?
## A method is a function in a class
class Student:
    def greet(self):
        print("Hello Student")

# Calling it:
s1 = Student()
s1.greet()

# 9️⃣ MOST IMPORTANT CONCEPT — self

# What is self?
## self represents the current object calling the method
### When we write:
s1.greet()
#Python internally converts it to:
Student.greet(s1)
# So:
self = s1

# Why self is needed?
## Because Python must know:
### which object is calling the method
### which object's data to use

# Without self, Python is blind

'''
“In a class, we define methods.
When an object calls a method, Python automatically passes that object as the first argument.
We receive that argument using self, which allows us to access the object’s data and methods.”
'''
#### self connects a method to the object that is calling it, not to the class

## Simple Example To Understand Self

class Demo:
    def show(self):
        print("Hello")
obj = Demo()
obj.show()

# Here:
obj.show()  #here what python is actually does means it uses it as Demo.show(obj)
# So self = obj


# 10 **** Constructor ****
## A constructor is a special method that runs automatically when an object is created
## We don't call it manually
## Python calls it for us

class Student():
    def __init__(self):
        print("Constructor is running")
    def greet(self):
        print("Hello Student")
# Now create an object
s1 = Student()
# s1.__init__() ## It is really bad practice because constructors are meant for initialization only
# Here we just wrote **s1 = Student()** means we just have created an object and does not call anything but we got "Constructor is running" because
# We have used __init__ method that is automatically calls the method whenever an object is created

# What if there is NO constructor?
# class Test:
#     pass

# t = Test()
# print("Object created")

# ✔ Object still gets created
# ❌ No initialization happens

# 2️⃣ Why do we need a constructor?
## Without constructor, all objects look the same
# ❌ Without constructor (problem)
# class Student:
#     name = "Unknown"
#     age = 0

# s1 = Student()
# s2 = Student()

# print(s1.name)
# print(s2.name)

# 👉 Both objects have the same data
# 👉 This is not realistic

# What __init__ actually does
### __init__ initializes(gives starting values to) an object

# That's why it is called initializer

## Basic syntax of __init__
# class ClassName:
#     def __init__(self):
#         pass

# __init__ is a special method
# self --> current object
# Runs automatically when object is created

# Simple example
class Student:
    def __init__(self):
        self.name = "Vali"
        self.age = 22
s1=Student()
'''
What happens internally:

   Object is created

   __init__ is called automatically

   Data is stored in the object
'''
print(s1.name)
print(s1.age)


# Constructor with parameters
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1 = Student("Vali",22)
s2 = Student("Rahul",23)
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

# Now:
## s1 has its own data
## s2 has its own data

# How self and __init__ work together

## self.name = name

# Means:
### Store name inside this object
## Each object has its own self

s1 = Student("Vali",22)
#Internally
Student.__init__(s1,"Vali",22)
# So:
### self = s1
### name = "vali"
### age = 22

# What happens if we dont use self in __init__?
## Wrong code
# class Student:
#     def __init__(self,name):
#         name = name
# Problem:
### name becomes a local variable
### Object does NOT store it

# Result:
## s1=Student("vali")
## print(s1.name) # Error


## Exercise Problems

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.name,self.age)
s1=Person("vali",22)
s2=Person("shaik",26)
s1.display_info()
s2.display_info()

########## Why self is required in __init__?
'''
self is required in __init__ because variables without self become local variables.
Using self stores the data inside the object, allowing the object to access it later.
Without self, the object would not have any stored data.
'''

############# self turns local data into object data ####################



#### Instance Variables vs Class Variables

## Instance variables belong to an object
## Class variables belong to the class and are shared by all objects.

#### Instance Variables
## Instance variables store data that is UNIQUE to each other
## They are created using self,usually inside __init__

# Example (Instance Variables)

class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age     # instance variable
s1 = Student("Vali",26)
s2 = Student("Rahul",21)
print(s1.name,s1.age)
print(s2.name,s2.age)
### Each object has its own copy of name and age

#### Why instance variables need self
## Because:
# Without self, variables become local
# With self, data is stored inside the object
## self = "this object"

#### Class Variables
## What are class variables
# Class Variables are shared by ALL objects of the class
# They are defined inside the class but outside any method

# Example (Class Variables)

class Student:
    college  = "ABC College" # class variable

    def __init__(self,name):
        self.name = name # instance variable

s1 = Student("Vali")
s2 = Student("Rahul")

print(s1.college,s1.name)
print(s2.college,s2.name)

# Both objects share the same college

## Key Difference 
'''
| Feature           | Instance Variable | Class Variable |
| ----------------- | ----------------- | -------------- |
| Defined using     | `self.variable`   | `variable`     |
| Belongs to        | Object            | Class          |
| Unique per object | ✅ Yes             | ❌ No           |
| Shared            | ❌ No              | ✅ Yes          |
| Stored in         | Object memory     | Class memory   |

'''

# Modify Instance vs Class Variable

### Modifying Instance Variable
s1.name = "NewName"
print(s1.name)
## ➡ Only s1 changes.

### Modifying class variable (WRONG way)
s1.college = "XYZ"
print(s1.college)  # It will still print the output but in behind the scenes it will not work as good because when we did it it will update our "ABC College" to "XYZ College" then we assume that all students belong to same college but for s1 it will print the updated college and for s2 it will print the previous college i.e. "ABC College " then this is logically wrong, so to get rid of this issue we need to modify in 
# proper manner i.e Student.college = "XYZ College" then for all students it will print same college
'''
✅ Python did this instead:

It created a NEW instance variable called college only for s1.

So now:

s1 has its own college

s2 still uses the class variable

This is called:

⚠️ Variable Shadowing

The instance variable shadows (hides) the class variable only for that object.
'''
print(s2.college)

# ⚠ This creates a new instance variable, NOT changing the class variable.

# s1.college = "XYZ College" when i print this i am getting output then why should we not use like this???
'''
Yes, s1.college = "XYZ" prints output,
but it does NOT change the class variable.
It creates a new instance variable, which is why we should not use it.
'''

'''
| Action                    | Result                       |
| ------------------------- | ---------------------------- |
| `s1.college = "XYZ"`      | ❌ Creates instance variable  |
| `Student.college = "XYZ"` | ✅ Updates class variable     |
| `print(Student.college)`  | Shows true class value       |
| `print(s1.college)`       | Instance overrides if exists |

'''

## Correct way to modify class variable

# Student.college = "XYZ College"
# #Now:
# print(s1.college)
# print(s2.college)

# Output
## XYZ College
## XYZ College


## Memory Understanding
# Instance Variables ---> stored inside object
# Class Variables ------> stored once inside class

### That's why class variables save memory


## When to use WHICH?

# Use instance variables when:
### Data differs per object
### Example: name, age, marks

# Use class variables when:
### Data is common for all
### Example: college name,company name,country

# Final Example:
class Employee:
    company = "Google"      # class variable

    def __init__(self, name):
        self.name = name    # instance variable

e1 = Employee("Vali")
e2 = Employee("Rahul")

print(e1.name, e1.company)
print(e2.name, e2.company)

# If data is common ---> class variable
# If data is unique ---> instance variable

# Exercise
class Car:
    wheels = 4

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

c1 = Car("TATA","INDICA VISTA")
c2 = Car("BMW","3 Series")

print(c1.brand,c1.model,c1.wheels)
print(c2.brand,c2.model,c2.wheels)


## What happens if we write :
# c1.wheels = 6
# Does it change for all cars or only one? Why?
# No, it will change for only car then after when we print another car existing wheels will be printed i.e. "4" instead of "6". This is due to we have written in wrong way here it will create one instance variable for that one object only remaining will use existing one so, we need to use like:
Car.wheels = 6
print(c1.wheels)
print(c2.wheels)



### __str__() Method

## Why __str__() exists???
# Look at this code
class Person:
    def __init__(self,name):
        self.name = name
p1 = Person("vali")
print(p1)

# Here we will get output as:

# <__main__.Person object at 0x000001F3A9C8>

# This output is :
### is not readable
### is not useful
### is not human-friendly

# What is __str__()?
## __str__() is a special method that defines how an object should be printed as a string

# Whenever we use :  print(object)
# Python internally calls:
# object.__str__()

# Simple Example of __str__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
p1 = Person("Shaik",22)
print(p1)

# Now we will get output as 
# Name : Vali, Age : 22 instead of <__main__.Person object at 0x000001F3A9C8> because here we have used __str__() method that's why our output is now readable,human-understandable,clean


# __str__() must RETURN a string, not print it

def __str__(self):
    print(self.name)
# Here we will get an error because we have used print so we need to use return instead of print

# When is __str__() automatically called?
## Python calls __str__() automatically when:
# We use print(object)
# We convert object to string using str(object)
# Example:
#print(p1)
#print(str(p1))

# Both do the same thing


# Without vs With __str__()

# Without __str__

# <__main__.Person object at 0x7ff9c3>

# With __str__
# Name: Vali, Age: 22

'''
Real-World Analogy (Easy to Remember)

Think of __str__() as:

“How should this object introduce itself to humans?”
'''

########### __str__() controls what gets printed when an object is printed #################

# Exercise Problems
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    
b1 = Car("BMW","3 Series",2023)
print(b1)


# What happens if __str__() is not defined?
# If we not define __str__() it is very difficult to understand, read by user whenever we print object so when we define __str__() it is easy to understand,read by user

'''
If __str__() is not defined, Python prints the default object representation, which shows the class name and memory address.
This output is not human-readable.
Defining __str__() allows us to control how the object is displayed in a clear and meaningful way.
'''



############ Encapsulation ################

# Encapsulation means keeping data safe by controlling how it is accessed or changed

# In short:
### We hide internal details
### We allow access only in a controlled way

# Real-life analogy
'''
🏧 ATM Example

You cannot directly access money inside the bank

You use:

   * ATM card

   * PIN

   * Withdraw option

👉 Money is hidden
👉 Access is controlled

That is encapsulation.
'''

# Why do we need Encapsulation?

## Encapsulation helps to:
### Protect data from accidental changes
### Avoid misuse of variables
### Make code safer and cleaner
### Control how values are updated


# Encapsulation in Python

## ⚠️ Python does not have strict private variables like Java.
### Instead, Python uses **naming conventions**

'''
In Java, private variables are strictly enforced by the compiler and cannot be accessed outside the class.
In Python, private variables use name mangling and are not strictly enforced, relying on developer discipline instead.
'''
'''
Java enforces privacy; Python suggests privacy.
'''

# Types of variables in Encapsulation

'''
1️⃣ Public
2️⃣ Protected
3️⃣ Private
'''

# Public Variables (Default)

## Accessible from anywhere

class Person:
    def __init__(self,name):
        self.name = name #public
p = Person("Vali")
print(p.name)

# Anyone can access
# No protection


# Protected Variables (_)
'''
🔹 What are they?

Variables meant to be used inside the class and its child classes

Access is discouraged, not blocked

🔹 How to recognize?

Starts with single underscore _
'''
### Accessible, but should not be touched directly (by convention)

class Person:
    def __init__(self,name,age):
        self._age = age #protected

# Usage
p = Person("Vali",22)
print(p._age) # works, but NOT recommended

# We can access it, but we should not
# _age means:
### Please don't access this directly unless we know what we are doing what

# Private Variables(__)
## What are they?
### Variables that should be accessed only inside the class
### Strongest form of protection in Python

## How to recognize?
### Starts with double underscore(__)

class Person:
    def __init__(self,salary):
        self.__salary = salary # private variable
    def show_salary(self):
        print(self.__salary)

p = Person(50000)
p.show_salary() #allowed
#print(p.__salary) #error

'''
in private to access it we are using methods and if we 
use direct p.__salary it will get an error .
here you have said that protection is in p.__salary 
but my doubt is when we can access salary using methods 
then how we can say that it is a private 
'''
#### Answer ####

'''
here __salary is hidden
show_salary is controlled access

User can:
* Read salary safely
* But cannot directly change it without rules 
'''

### Answer Clarification and Doubt

'''
means user can jsut read salary using methods but user cant directly change it.
Here to chnage it we are using instance variables topic to modify it but this modification is not allowed in private. Am I right?
'''

'''
1. Can user READ a private variable?

✅ YES — but only through methods

2. Can user DIRECTLY change a private variable?

❌ NO

p.__salary = 100000   # ❌ NOT allowed


3. Can a private variable EVER be changed?

✅ YES — but ONLY through class methods

Example:
'''
class Person:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

# 1️⃣ Create object
p = Person(50000)

# 2️⃣ Read salary (controlled access)
print(p.get_salary())

# 3️⃣ Modify salary (controlled update)
p.set_salary(0)

# 4️⃣ Read updated salary
print(p.get_salary())

'''
__salary → private

❌ p.__salary → not allowed

✅ get_salary() → read safely

✅ set_salary() → modify safely with rules
'''

############# Private variables must be accessed and modified only through class methods #####################

# How to access private data properly? (Getter & Setter)

## Getter (read value)
## Setter(modify value)

class Person:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary!!!!")

p = Person(50000)
print("Original Salary: ",p.get_salary())
p.set_salary(60000)
print("Updated Salary: ",p.get_salary())

#### Why Encapsulation is IMPORTANT
# ENCAPSULATION:
'''
Protects internal data

Improves maintainability

Prevents invalid data

Makes code robust
'''

######## Encapsulation = hide data + control access  ##############


# Exercise:

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: ",amount)
        else:
            print("Invalid Deposit")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawan: ",amount)
        else:
            print("Insufficient Depsoit")

    def get_balance(self):
        return self.__balance
b = BankAccount(78000)
b.deposit(30000)
b.withdraw(20000)
print("Final Balance: ",b.get_balance())

# Why should be balance be private?
## We need to keep balance private allowing that another user can't see balance amount of another ones for this we have used __balance (private variable)
'''
Balance should be private to prevent direct access or modification by users.
This ensures security, avoids invalid changes, and allows controlled updates through methods.
'''

class Employee:
    company_name = "TechCorp"
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary!!!")
    def give_bonus(self,amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Bonus should not be zero😁😊")
    def __str__(self):
        return f"Employee: {self.name} | ID: {self.employee_id} | Company: {Employee.company_name}"
e = Employee("Vali",101,80000)
print(e)
print("Salary:",e.get_salary())
e.set_salary(90000)
e.give_bonus(5000)
print("Final Salary:",e.get_salary())


############### DAY 12 CONCEPTS #######################
'''
✔ OOP Foundations

Why OOP exists

Class & Object

Methods inside a class

✔ Core OOP Mechanics

self (deep understanding)

Constructor (__init__)

Object creation & initialization

✔ Data Handling

Instance variables

Class variables

Correct modification rules

✔ Python Special Methods

__str__() for clean object printing

✔ Encapsulation

Public, Protected, Private variables

Name mangling (__variable)

Getter & Setter methods

Controlled data access

✔ Hands-on Practice

Person, Car, BankAccount, Employee classes

Real-world logic (salary, balance, bonus)

Error identification & correction
'''