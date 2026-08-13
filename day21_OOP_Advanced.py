# 1. Abstraction
## Abstarction = hiding HOW something works and only showing WHAT you can do
### Real-life example:
# We press "Withdraw 500"
# We don't see : authentication,server request, cash log, account update
## Complexity is hidden

# Example
class Car:
    def start(self): # user sees only this
        self.__engine() # internal work (hidden) (This is a private method also known as name mangling rule --- it cannot be accessed directly using the object)
    def __engine(self): # private helper --> hidden
        print("Engine Started...")
c = Car()
c.start()
# c.engine() --> It will throw an error that 'Car' object has no attribute 'engine'

'''
🔥 Why this is part of Abstraction? (this refers to self.__engine() because it is a private method)

Because abstraction = hiding complexity from user
✔ User only sees start()
✔ Internal logic __engine() is hidden
✔ User cannot misuse or call it
'''

# 2. Abstract Class
## A normal class = can be used to create objects
### Example:
class Car:
    pass
c = Car() # here object will be created
### BUTTTTTTTT
# A "abstract class" = cannot be used to create objects
# It is only used aa a blueprint for other classes

# Why Do We Need Abstract Classes?
## Imagine we are building a big project (banking, e-commerce, payments..)
## We want every child class to follow same rule
## Example:
### Every payment method must have a .pay() function
#### PhonePe --> must have pay
#### GooglePay --> must have pay
#### PayTM    ---> must have pay

# If any developer forgets to write pay(), the app will break
## So we create a parent abstract class that forces child classes to implement that method

# Syntax -- Abstract Class (using abc module)
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
# p = Payment() # Error : Caanot create object ( Can't instantiate abstract class Payment with abstract method pay )

# Because Python says:
## "We cannot create object because this class has unfinished functions"


# Implementing Child Classes
class PhonePe(Payment):
    def pay(self,amount):
        print("Paid",amount,"via PhonePe")
class Googlepay(Payment):
    def pay(self,amount):
        print("Paid",amount,"via Google Pay")

p = Googlepay()
p.pay(50000)

'''
in syntax from abc import ABC,abstarctmethod are constant like can we change it like from xyz import XYZ,abstarctmethod
'''

######## ANSWER #######

'''
✔ abc is the official Python module name

(stands for Abstract Base Classes)

✔ ABC and abstractmethod are class & decorator names defined inside that module
'''

'''
abc module = only source of abstract class features
ABC = base abstract class
@abstractmethod = decorator forcing implementation

'''

# 3 Interface

# Abstract Class (has some code already)
from abc import ABC,abstractmethod
class Animal(ABC):
    def breathe(self): # already working
        print("Breathing...")
    @abstractmethod
    def sound(self): # MUST be implemented later
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.breathe() # working from parent
d.sound() # child implementation

# Here parent already gave breathe() --> some code exists
#### So this is Abstract Class #######


# Interface-Style Class ( NO CODE -- ONLY RULES )

from abc import ABC,abstractmethod

class LoginSystem(ABC):
    @abstractmethod
    def login(self):
        pass

# Child classes

class EmailLogin(LoginSystem):
    def login(self):
        print("Logged in with Email")
class OtpLogin(LoginSystem):
    def login(self):
        print("Logged in with Otp")

l = EmailLogin()
l.login()

# Parent gives NO working code
# Only RULE : " We MUST have login()"
# This behaves like Interface

'''
ABSTRACT CLASS = can have both complete methods + abstract methods
INTERFACE (Python style) = only abstract methods (no body / no logic)

'''

'''
Interface = only rules
Abstract class = rules + some ready-made code
'''

# 4. Polymorphism
## Poly = many
## Morph = forms
### Polymorphism = Same name, different behaviors

# Example in real life:
'''
| Action | Who?  | Behavior   |
| ------ | ----- | ---------- |
| eat()  | Dog   | eats bones |
| eat()  | Human | eats food  |
| eat()  | Snake | swallows   |

Same function name --> behvaes differently based on object
'''
# Polymorphism in Python
## Example 1: Method Overriding
class Animal:
    def sound(self):
        print("Some sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
animals = [Dog(),Cat(),Animal()]
for a in animals:
    a.sound()
# d = Dog()
# d.sound()
# c = Cat()
# c.sound()

# Output depends on which object is calling

# Example 2: One function,many object types
class Car:
    def start(self):
        print("Car started")
class Bike:
    def start(self):
        print("Bike Started")
def begin(vehicle):
    vehicle.start()
begin(Car()) # Car Started
begin(Bike()) # Bike Started

# One function (begin()) works for multiple types

# Example 3: Built-in Python Polymorphism

print(len("Python"))
print(len([1,2,3]))
print(len({1:10,2:20}))
# len() changes behavior based on input type

###### Why Polymorphism Is Important ? #######
'''
✔ Code becomes reusable
✔ Reduces many if-else checks
✔ Cleaner design
✔ Used in frameworks, GUI apps, ML models, Django, APIs
'''

from abc import ABC,abstractmethod
class Shape (ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Sqaure(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5*self.b*self.h
shapes = [Circle(5),Sqaure(4),Triangle(3,6)]
for shape in shapes:
    print(shape.area())



#### Exercises
# Exercise 1
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("This is a bike class")
class Car(Vehicle):
    def start(self):
        print("This is a Car Class")
v = [Bike(),Car()]
for property in v:
    property.start()


# Exercise 2
from abc import ABC,abstractmethod
class LoginSystem(ABC):
    @abstractmethod
    def login(self,username,password):
        pass
class EmailLogin(LoginSystem):
    def login(self,username,password):
        print(f"{username} Logged in using Email & Password")

class MobileLogin(LoginSystem):
    def login(self,username,password):
        print(f"OTP sent to mobile number of {username}")
e = EmailLogin()
m = MobileLogin()
e.login("Vali","1234")
m.login("Shaik","otp")

'''
An interface not only forces method names, but also enforces how the method should be called.
'''

# Exercise 3

from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        return  0.5 * self.b * self.h
areas = [Circle(3),Square(6),Triangle(4,2)]
for a in areas:
    print(a.area())
      
# Exercise 4


class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def give_bonus(self,amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Salary Must Be Greater Than Zero")

    def __str__(self):
        return f"{self.name} {self.__salary}"
    
emp1 = Employee("Vali",50000)
emp2 = Employee("Shaik",45000)
emp1.give_bonus(5000)
emp2.give_bonus(4000)
print(emp1)
print(emp2)

'''
# ==========================================================
# DAY 21 — OBJECT ORIENTED PROGRAMMING (ADVANCED)
# ==========================================================

# ──────────────────────────────────────────────────────────
# 1️⃣ ABSTRACTION
# ──────────────────────────────────────────────────────────
# Abstraction = Hiding internal details & showing only
# essential behavior to the user.
#
# Implemented using abstract classes (abc module)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Abstract class:
# - Cannot create object
# - Can contain abstract + normal methods
# - Forces child classes to implement required methods

# ──────────────────────────────────────────────────────────
# 2️⃣ ABSTRACT CLASS
# ──────────────────────────────────────────────────────────
# Rules:
# - Must inherit from ABC
# - Abstract methods must use @abstractmethod
# - Object of abstract class cannot be created

class Animal(ABC):
    def breathe(self):          # Normal method allowed
        print("Breathing")

    @abstractmethod
    def sound(self):
        pass

# ──────────────────────────────────────────────────────────
# 3️⃣ INTERFACE (Python Style)
# ──────────────────────────────────────────────────────────
# Python has NO 'interface' keyword.
# Interface behavior is achieved using abstract classes
# with ONLY abstract methods.

class LoginSystem(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

# Child classes MUST implement login()

# ──────────────────────────────────────────────────────────
# 4️⃣ METHOD OVERRIDING
# ──────────────────────────────────────────────────────────
# Child class provides its own implementation of parent method

class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

# ──────────────────────────────────────────────────────────
# 5️⃣ POLYMORPHISM
# ──────────────────────────────────────────────────────────
# Same method name, different behavior based on object

class Dog:
    def sound(self): print("Bark")

class Cat:
    def sound(self): print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()   # Polymorphism

# Polymorphism happens when:
# ✔ Same method name
# ✔ Different objects
# ✔ Different outputs

# ──────────────────────────────────────────────────────────
# 6️⃣ ENCAPSULATION
# ──────────────────────────────────────────────────────────
# Encapsulation = Protect data using private variables
# and allow controlled access using methods

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # private

    def get_salary(self):
        return self.__salary

    def give_bonus(self, amount):
        if amount > 0:
            self.__salary += amount

    def __str__(self):
        return f"{self.name}, Salary: {self.__salary}"

# Private variables:
# __salary → cannot be accessed directly
# emp.__salary ❌

# ──────────────────────────────────────────────────────────
# 7️⃣ __str__() METHOD
# ──────────────────────────────────────────────────────────
# Makes object printable in readable format

# Without __str__():
# <__main__.Employee object at 0x123>

# With __str__():
# Employee: Vali, Salary: 55000

# ──────────────────────────────────────────────────────────
# 🔑 GOLDEN RULES (VERY IMPORTANT)
# ──────────────────────────────────────────────────────────
#
# ✔ Abstract class = blueprint
# ✔ Interface = abstract class with only abstract methods
# ✔ Abstract method → no logic, only rule
# ✔ Cannot create object of abstract class
# ✔ Method signature must be SAME in parent & child
# ✔ Polymorphism = loop + same method call
# ✔ Encapsulation = private data + public methods
#
# ==========================================================

'''