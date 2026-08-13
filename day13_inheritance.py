############### Inheritance (OOP) #######################

# What is Inheritance ?
## Inheritance allows one class to use the properties and methods of another class

### One class inherits from another
### This avoids rewriting the same code

# Real-life example
'''
👨‍👩‍👧 Family example

Parent has:

  surname

  house

Child automatically gets:

  surname

  house

Child doesn’t need to redefine them.

👉 This is inheritance.
'''

# Why do we need Inheritance?
## Inheritance helps to:
### Reuse code
### Reduce duplication
### Organize classes in hierarchy
### Make code easier to maintain

# Basic Syntax of Inheritance
class Parent:
    pass
class Child(Parent):
    pass
# Parent ---> base / parent class
# Child ----> derived / child class

# Example:
## Parent Class
class Animal:
    def eat(self):
        print("Animal eats food")
## Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")
a = Dog()
a.eat() # inherited from animal
a.bark() # Dog's own method

# Dog can use:
### It's own methods
### Parent's Methods

# What child class INHERITS
# From parent:
## Methods
## Variables
## Behaviors

# Child can also:
## Add new methods
## Override existing methods

# Types of Inheritance

## Single Inheritance
## Multilevel Inheritance
## Hierarchial Inheritance
## Multiple Inheritance

# Single Inheritance

class Person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("Name :",self.name)
class Student(Person):
    def study(self):
        print("Student is studyinggg")
s = Student("Vali")
s.show_name()
s.study()

'''
class Person:
    # def __init__(self,name):
    #     self.name = name
    def show_name(self,name):
        self.name = name
        print("Name :",self.name)
class Student(Person):
    def study(self):
        print("Student is studyinggg")
s = Student("Vali")
s.show_name()
s.study()

I wantedly keep constructed as comments to see what happens when it is commented. 
That's why I have commented those in init() method. 
And I have written self, name in showName() method. 
And I have raised type error student takes no arguments. 
Means I have a small doubt that we are importing student of vali.
Student of vali means we are inheriting student of person. 
In person we have commented init() method. Then we have only one method that is showName() In showName() we have self, name. 
Then why it is raising type error? Because I just want to know without this constructor what happens whenever we just initialized, whenever we declared method only in class, parent class.
'''

#### Answer

'''
If a class does not define __init__, Python automatically provides a default constructor that takes ONLY self.

That default constructor looks like this internally:

def __init__(self):
    pass

#########

🔍 Step-by-step: What Python is doing
Step 1: You commented out Person.__init__
So now:

Person has NO constructor

Student also has NO constructor

Step 2: Python gives BOTH classes a default constructor
Equivalent to:

class Person:
    def __init__(self):
        pass

class Student(Person):
    def __init__(self):
        pass
Step 3: You create the object

s = Student("Vali")
Python internally tries to do:

Student.__init__(s, "Vali")
But actual constructor is:

def __init__(self):
    pass
❌ It accepts only self
❌ You passed one extra argument ("Vali")

➡️ TypeError: Student() takes no arguments

🧠 Common misunderstanding (you had this doubt)

“Student inherits Person, Person has show_name(self, name), so why can’t Student("Vali") work?”

Because:

❌ Constructor parameters ≠ method parameters

They are completely different things.

#####################################################################################
If __init__ is not defined, Python uses a default constructor that takes no arguments.
Passing arguments while creating the object will raise TypeError.
'''

#### Inheritance with super()

# What is super()?
## super() is used to call the parent class methods from the child class

# Most commonly, it is used to call the parent constructor (__init__)

# Why do we NEED super() ?
## Because:
### Parent class may initialize important data
### Child class should not rewrite that logic
### We want to reuse parent constructor

# Example WITHOUT super() 
# class Perosn:
#     def __init__(self,name):
#         self.name = name
# class Student(Person):
#     def __init__(self,roll):
#         self.roll = roll
# s = Student("Vali")

# ❌ name is never set
# ❌ Parent constructor is NOT called

# So self.name does not exist

# Correct Example WITH super()
class Person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("Name: ",self.name)

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def study(self):
        print("Student is studying")

s = Student("Vali",22)
s.show_name()
print("Roll: ",s.roll)
s.study()

'''
If a child class has its own __init__, it must call super().__init__() to initialize parent data.
'''

# super() is NOT only for constructors
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
d = Dog()
d.sound()

'''
super() calls parent

Without super(), parent init is skipped

Use super() inside child __init__
'''

class Vehicle:
    def __init__(self,speed):
        self.speed = speed
    def show_speed(self):
        print("Speed is :", self.speed)
class Car(Vehicle):
    def __init__(self,speed,brand):
        super().__init__(speed)
        self.brand = brand
    def show_brand(self):
        print("Brand Name: ", self.brand)
v = Car(45,"BMW")
v.show_speed()
v.show_brand()

'''
When a child class has its own constructor, 
super() must be used to initialize parent attributes.
'''

############ Method Overriding ######################

# What is Method Overriding?
## Method overriding means the child class provides its own version of a
## method that already exists in the parent class

# In short:
### Same method name
### Same parameters
### Child replaces parent behavior

# Why do we need Method Overriding?
# Because:
## Parent behavior may be too general
## Child needs specific behavior
## Real-world objects behave differently

# Simple Real-life Example
## Animal --> makes sound
## Dog --> barks
## Cat ---> meows
# Same action(sound()), different behavior
#### This is method overriding #####

# Basic Example
# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")
# Child Class (Override)
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Dog()
a.sound()

# Output
## Dog barks

### Parent method is replaced by child method

##### If child and parent have the same method name, the child's method is called
### This is called runtime polymorphism

# How Python decides which method to call
# Python checks in this order:
## Child class
## Parent class
# If found in child --> stop searching

# Overriding + super()
# Sometimes we want:
## Parent behavior
## PLUS child behavior
# Example
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

# Output
'''
Animal makes a sound
Dog barks
'''
# super() lets you extend, not replace

# Overriding with __init__
## Constructors can also be overridden
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
# Child constructor overrides parent constructor
# super() keeps parent initialization alive

## Same name ----> override
## Child wins
## use super() to keep parent logic


# Exercise 1
'''
Create:

class Employee

method get_role() → prints "Employee"

class Manager(Employee)

override get_role() → prints "Manager"

Create object of Manager and call method.
'''
class Employee:
    def get_role(self):
        print("Employee")
class Manager(Employee):
    def get_role(self):
        print("Manager")
v = Manager()
v.get_role()

# Exercise 2
'''
Modify Exercise 1 to:

call parent method also using super()
'''
class Employee:
    def get_role(self):
        print("Employee")
class Manager(Employee):
    def get_role(self):
        super().get_role()
        print("Manager")
v = Manager()
v.get_role()

'''
Method overriding allows a child class to provide a specific implementation of a method already defined in the parent class.
Using super() lets the child reuse parent behavior while extending it.
'''

############### Multilevel Inheritance #######################
# What is Multilevel Inheritance?
## Multilevel inheritance means a class inherits from a class that already inherited from another class

# In short:
# Grandparent --> Parent --> Child

# Each level passes features down

# Real-life Example
'''
👴 Grandfather → 👨 Father → 👦 Son

Son gets properties from Father

Father already got properties from Grandfather

👉 Son indirectly gets both.
'''

# Basic Structure
class A:
    pass
class B(A):
    pass
class C(B):
    pass

'''
A → Base class

B → Derived from A

C → Derived from B
'''
# Simple Working Example
class Animal:
    def eat(self):
        print("Animal eats")
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")
class Dog(Mammal):
    def barks(self):
        print("Dog Barks")
d = Dog()
d.eat()
d.walk()
d.barks()

'''
👉 Dog can access:

its own methods

parent methods

grandparent methods
'''

# Constructor in Multilevel Inheritance(super()chain)
class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("C constructor")
c = C()
# super() moves level by level upward

# Method Overriding in Multilevel Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    def show(self):
        print("Class C")
c = C()
c.show()
# Python always choose the lowest-level child

# Using super() with overriding
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    def show(self):
        super().show()
        print("Class C")
c = C()
c.show()

# IMPORTANT RULES
## Child inherits everything above it
## Lowest class method is called first
## super() moves upward one level
## Constructors must use super()

## Exercise Problems
'''
Create:

Device → method power_on()

Computer(Device) → method boot()

Laptop(Computer) → method portable()

Create object of Laptop and call all methods.
'''

# Exercise 2
'''
Add constructors to all three classes and use super() correctly.
'''
class Device:
    def power_on(self):
        print("Power On Device")
class Computer(Device):
    def boot(self):
        print("Booting is Added")
class Laptop(Computer):
    def portable(self):
        print("Portable Featured")
e = Laptop()
e.power_on()
e.boot()
e.portable()


class Device:
    def __init__(self):
        print("Power On Device")
class Computer(Device):
    def __init__(self):
        super().__init__()
        print("Booting is Added")
class Laptop(Computer):
    def __init__(self):
        super().__init__()
        print("Portable Featured")
e = Laptop()


############# Hierarchial Inheritance ################
# What is Hierarchial Inheritance?
## Hierarchial Inheritance means one parent class is inherited by multiple child classes

# In short:
'''
        Parent
        /   \
     Child1 Child2

'''
# Real-life example
'''
👨 Person
├── 👨‍🎓 Student
└── 👨‍💼 Employee

Student and Employee both inherit from Person

They share common features

Each has its own specific behavior
'''

# Basic Structure
class Parent:
    pass
class Child1(Person):
    pass
class Child2(Person):
    pass

# Simple Working Example
class Father:  # Parent
    def show_name(self):
        print("I am a father")
class Son(Father): # Child1
    def job(self):
        print("I am a Son")
class Daughter(Father): # Child2
    def cooking(self):
        print("I am a daughter")
f = Son()
g = Daughter()
f.show_name()
f.job()
g.show_name()
g.cooking()

# Both children use same parent method, but have different behaviors

class Person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("Name: ",self.name)

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id = emp_id
p = Student("Vali","Developer")
q = Employee("Rahul",101)
p.show_name()
print("Roll: ",p.roll)
q.show_name()
print("Employee_id: ",q.emp_id)

# IMPORTANT RULES
### One parent --> many children
### Children cannot access each other
### Parents methods are shared
### Use super() to initialize parent data


#### Hierarchial Inheritance = one parent, many children

###### Exercise Problems ########
# Exercise 1
class Account:
    def account_type(self):
        print("This is SBI Account")
class SavingsAccount(Account):
    def interest(self):
        print("This is interest type account")
class CurrentAccount(Account):
    def overdraft(self):
        print("This is Current Account")
s = SavingsAccount()
t = CurrentAccount()
s.account_type()
s.interest()
t.account_type()
t.overdraft()

# Exercise 2
## Can SavingsAccount access Overdraft()? why or why not?
## NO, we cannot access overdraft() with SavingsAccoount because overdraft() is belongs to the CurrentAccount (child2) and with child1 (SavingsAccount) we can access only interest(). Here in hierarchial inheritance childs can access parents behavior, but one child can't access behavior of another child

'''
In hierarchical inheritance, child classes inherit only from the parent class.
One child class cannot access the methods of another child class because there is no inheritance relationship between siblings.
'''

############### MUltiple Inheritance ########################

# What is Multiple Inheritance?
## Multiple Inheritance means a child class inherits from MORE THAN ONE parent class
'''
Parent1   Parent2
    \       /
      Child
'''
# Real-life example
'''
👨 Person → name
💼 Employee → salary

👨‍💻 SoftwareEngineer

needs name (Person)

needs salary (Employee)

👉 One child, two parents.
'''
# Basic Syntax
class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1, Parent2):
    pass

# Order matters

class Father:
    def skills(self):
        print("Father: Driving")
class Mother:
    def skills(self):
        print("Mother: Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skills()

# Output:
# Father : Driving

# Why Father First?
### Because Python follows MRO (Method Resolution Order)

####### Method Resolution Order (MRO) ##############
# MRO decides which parent method is called when method names are same

## Python searches in this order:
# 1. Child Class
# 2. First parent
# 3. Second parent
# 4. Grandparents

# We can check MRO using:
print(Child.mro())


# Changing The Parent order Changes Output
class Child(Mother, Father):
    pass
c.skills()
# Output:
# Mother : Cooking

## Order of parents matters in multiple inheritance

### Multiple Inheritance with Different Methods
class A:
    def show_a(self):
        print("A class")

class B:
    def show_b(self):
        print("B class")

class C(A, B):
    pass
c = C()
c.show_a()
c.show_b()

## Output:
# A class
# B class

'''
✔ No conflict
✔ Very safe
'''

## Multiple Inheritance with Constructors (super())
class A:
    def __init__(self):
        print("A init")
class B:
    def __init__(self):
        #super().__init__() # if we call using super() it will still not print because in python multiple inheritance uses "MRO" to access all parents we need to use super() for all classes or there are different methods for each parent,
        # if there are same methods we think that if we use super() it will gets printed but not because it follows "MRO"
        print("B init")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")

c = C()

# Output 
## A init
## C init

# *** B.__init__() is skipped
# Why? Because super() follows MRO , not "all parents"

### *** To make ALL constructors run, every class must use super()***********

class A:
    def __init__(self):
        super().__init__()
        print("A init")

class B:
    def __init__(self):
        super().__init__()
        print("B init")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

c = C()

# Output
'''
B init
A init
C init
'''
# Why this order?
# MRO:
# C --> A --> B --> object
'''
Execution:

C.__init__() → A.__init__() → B.__init__() → object.__init__()
'''

'''
In multiple inheritance, super() follows the MRO and calls the next class in the order.
To ensure all parent constructors run, every class must use super() cooperatively.
'''
####### *****Correct Way (Advanced Concept)******* ###########

# To call all constructors, all classes must use super() properly (cooperative inheritance)
# But, for now we should remember this:
### In multiple inheritance, super() follows MRO, not all parents will print even we use super()

# When to use Multiple Inheritance?
'''
✅ Use when:

Parent classes are independent

Methods don’t clash

You understand MRO

❌ Avoid when:

Parents have many same method names

Code becomes confusing
'''

## One-line Memory Rules 
'''
Multiple inheritance = many parents

Order matters

MRO decides method call

super() follows MRO
'''

# Exercise Problems

# Exercise 1:

class Camera:
    def feature(self):
        print("Capturing")
class Phone:
    def feature(self):
        print("Recording")
class SmartPhone(Camera,Phone):
    def feature11(self):
        print("There are so many features in SmartPhone")
m = SmartPhone()
m.feature()

# Exercise 2
# Print MRO of SmartPhone
print(SmartPhone.mro())


##### ***** MRO defines the order; super() walks that order one step at a time ********* #############