# What is Module?
## A module is a .py file that contains functions/classes we want to reuse
### Example
# # calculator.py
# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# # Using it inside another file:
# import calculator
# print(calculator.add(10,5))

# A module keeps code clean, reusable, and avoids rewriting

# What is a Package?
## A package is a folder that contains multiple modules and a file called __init__.py
# __init__.py tells Python: "This folder is a package -- it contains importable Python code"

### Example:
'''
project/
    main.py
    math_pkg/
        __init__.py
        add.py
        sub.py
        divide.py

'''
# Creating Our Own Package

## Step 1 -- Create Folder
### calculator_pkg/
## Step 2 -- Add __init__.py
### calculator_pkg/__init__.py
# print("Package Loaded")
## Step 3 -- Create modules
### calculator_pkg/add.py
# def add(a,b): return a + b
### calculator_pkg/sub.py
# def sub(a,b): return a - b
## Step 4 -- Use them in main.py
### from calculator_pkg.add import add
### from calculator_pkg.sub import sub
### print(add(10,5))
### print(sub(8,3))


# Absolute vs Relative Import
## Absolute Import (full path)
### from calculator_pkg.add import add

## Relative Import (Inside a package)
### inside __init__.py
#### from .add import add
#### from .sub import sub
###### Then from main.py
## from calculator_pkg import add,sub
## print(Add(10,4))


# Controlling What Imports

## Inside __init__.py we can control what becomes public:
# __all__ = ["add"] # only add will be importable
# ## Now:
# from calculator_pkg import *
# print(add(10,3)) # works
# print(sub(8,2)) # Cannot import (blocked)

'''
🟡 Exercise-1 — Create a Calculator Package

Create folder:

calculator_pkg/
    __init__.py
    add.py
    sub.py
    mul.py


add.py

def add(a,b): return a+b


sub.py

def sub(a,b): return a-b


mul.py

def mul(a,b): return a*b


👉 In main.py, do:

from calculator_pkg.add import add
from calculator_pkg.sub import sub
from calculator_pkg.mul import mul

print(add(4,5))
print(sub(7,3))
print(mul(6,6))

🟡 Exercise-2 — Use Absolute Import + Alias
import calculator_pkg.add as A
print(A.add(10,2))

🟡 Exercise-3 — Use Relative Import Inside Package

Inside calculator_pkg/__init__.py:

from .add import add
from .sub import sub
from .mul import mul


Then update main.py:

from calculator_pkg import add, sub, mul
print(add(3,3))
print(sub(9,5))
print(mul(8,8))

🟡 Exercise-4 — Control What Gets Imported

Inside __init__.py add:

__all__ = ["add"]      # Only add becomes importable


Then:

from calculator_pkg import *
print(add(5,4))
print(sub(10,3))   # ❌ should give error


👉 Confirm: Why does sub() now fail?

🟡 Exercise-5 — Create Utilities Package
utils/
    __init__.py
    text.py
    math_utils.py


text.py

def reverse(text):
    return text[::-1]


math_utils.py

def cube(n):
    return n*n*n


✔ Use:

from utils.text import reverse
from utils.math_utils import cube

print(reverse("Python"))
print(cube(3))

🟡 Exercise-6 — Read File Using a Helper Module

Create:

filetools/
   __init__.py
   reader.py


reader.py

def read_file(path):
    with open(path,"r") as f:
        return f.read()


Main:

from filetools.reader import read_file
print(read_file("notes.txt"))

🟡 Exercise-7 — Create Program Entry File

Create:

project/
   app.py
   tools/
       __init__.py
       add.py


add.py

def add(a,b): return a+b


app.py

from tools.add import add
if __name__ == "__main__":
    print("App started")
    print(add(2,2))


✔ Output:

App started
4

🟡 Exercise-8 — Folder Import Error Case

Test:

import tools


❓ Does this work?
If not → why must tools folder contain __init__.py ❓
Write the answer in a comment.
Answer 

❓ Why import tools fails?

Because tools is just a folder — Python can't import folders.
Python only imports packages, and a folder becomes a package 
ONLY when it contains __init__.py. So import tools fails because 
__init__.py is missing.

🟡 Exercise-9 — Create a Package That Prints When Imported

Inside testpkg/__init__.py:

print("Package Loaded Successfully")


Then import:

import testpkg


📌 Expected:

Package Loaded Successfully

🟡 Exercise-10 — Bonus Challenge 🎯

Create a package:

textops/
    __init__.py
    case.py
    length.py


case.py

def to_upper(t): return t.upper()


length.py

def size(t): return len(t)


Use:

import textops.case as C
from textops.length import size

print(C.to_upper("day20"))
print(size("python"))

'''

############### DAY 20 -- MODULES & PACKAGES -- CHEAT SHEET ##################
'''
# ─────────────────────────────────────────────────────────────
# 📦 MODULES
# A .py file that contains reusable code (functions/classes)
# Example:
#   calculator.py → def add(a,b): return a+b
# Import:
#   import calculator
#   from calculator import add
# Alias:
#   import calculator as calc
# ─────────────────────────────────────────────────────────────

# 📂 PACKAGES
# A folder that contains multiple .py modules + __init__.py
# Structure:
#   mypkg/
#       __init__.py   ← required to make folder importable
#       add.py
#       sub.py
#   main.py

# ─────────────────────────────────────────────────────────────
# 🧭 IMPORT TYPES
# Absolute Import  → from mypkg.add import add
# Relative Import  → (inside package)
#   in __init__.py:
#       from .add import add
#       from .sub import sub
# ─────────────────────────────────────────────────────────────

# 🎯 __init__.py – WHY IMPORTANT?
# • Tells Python the folder is a package
# • Controls what is importable
# • Can run code when package loads
#
# Example – Allow only add():
#   __all__ = ["add"]
#
# Example – Package auto code:
#   print("Package Loaded")
# ─────────────────────────────────────────────────────────────

# 🧠 __name__ == "__main__"
# Makes sure certain code runs ONLY when file is executed directly
# NOT when imported in another file.
#
# Example:
#   if __name__ == "__main__":
#       print("App started")
# ─────────────────────────────────────────────────────────────

MODULE  = single Python file
PACKAGE = folder of modules (+ __init__.py)
ABSOLUTE IMPORT = full path
RELATIVE IMPORT = use inside package
__init__.py = makes folder importable + controls exports

'''