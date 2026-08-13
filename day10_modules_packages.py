# Modules & Packages
# 1. What is a Module?
## A module is just a Python file (.py) that contains:
### functions
### variables
### classes

## In simple words:
### Any Python file is a **module**

# Example
## Create a file called:
##### math_utils.py #####

# Inside it:
'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

'''

#### math_utils.py is now a module

# 2. Why do we use Modules?

## Modules help to:
### Organize code
### Avoid very large files
### Reuse code
### Maintain projects easily
### Work in teams

# Without modules ---> one huge messy file
# With modules ---> clean,readable structure

# 3. How to import a module
## Method 1: import module_name

import math_utils
print(math_utils.add(10,5))
print(math_utils.sub(10,5))

# We must use module_name.function_name

## Method 2: from module import function
from math_utils import add,sub
print(add(10,5))
print(sub(10,5))

# No need to write module name again as write in **Method 1**

# Method 3: import module as alias
import math_utils as mu
print(mu.add(10,5))
print(mu.sub(10,5))

# Alias is used to shorten the long module names


# 4. Importing Built-in Modules
## Python already gives many modules
# Example : math
import math
print(math.sqrt(16))
print(math.pi)
print(math.log(2))

# Example:random
import random
print(random.randint(1,10))

# Example:datetime
import datetime
now = datetime.datetime.now()
print(now)

# 5. What is __name__ == "__main__" !!! (VERY IMPORTANT)
# Example module:example.py
# def greet():
#     print("Hello")
# print("This is example.py")

## If we run this file directly:
#python example.py

#Output
#This is example.py

#Now modify it:
# def greet():
#     print("Hello")
# if __name__=="__main__":
#     print("This is example.py")

### Here when we import example module in this file it just prints hello and not print This is example.py because we have used __name__ == "__main__"

import example
example.greet()

#### Another simple example to understand __name__ == "__main__" ######
#calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculator started")

#main.py
#import calculator
#print(calculator.add(5, 3))

#Output is just ** 8 ** 

'''
Example WITHOUT __name__ == "__main__" (PROBLEM CASE)
calculator.py
def add(a, b):
    return a + b

print("Calculator started")

main.py
import calculator
print(calculator.add(5, 3))

Output when running main.py:
Calculator started
8

❌ Why this is a problem?

Because:

You only wanted the function add

But extra code also ran automatically

In big projects, this causes unexpected behavior

🧠 WHAT __name__ == "__main__" SOLVES

It lets you separate two things:

Reusable code (functions, classes)

Runnable code (testing, demo, execution)
'''

import example
example.add(5,2)
example.sub(5,3)

'''
🧠 What SHOULD go inside if __name__ == "__main__"?

✔ Function calls
✔ Print statements
✔ Input/output
✔ Test code
✔ Demo code

❌ Function definitions
❌ Class definitions (same rule applies)
'''

########### Understanding each piece if __name__=="__main__"

'''
"__name__ is a special variable that holds the name of the current module.
When a file is executed directly, its value is '__main__'.
This is used to control which code runs on direct execution versus import."
'''

'''
| Part         | Meaning                       |
| ------------ | ----------------------------- |
| `__name__`   | Special variable              |
| `==`         | Comparison                    |
| `"__main__"` | Main executing program        |
| Whole line   | Check if file is run directly |

'''


'''
if __name__ == "__main__":

# If this Python file is the main program being run
'''

# What is a Package? 
## A package is a folder that cotains multiple Python modules(files)

### Module ---> One Python file(.py)
### Package ---> Folder Containing Python Files
"""
🧩 Why do we need Packages?

Imagine this situation 👇

You are building a project and you have:

math functions

string functions

file functions

database functions

If you put everything in one file, it becomes:

messy

hard to manage

hard to understand

👉 Packages help organize related modules together.
"""
## Simple Package Structure
'''
my_package/
│
├── __init__.py
├── math_utils.py
├── string_utils.py

'''
## What is what?

### my_package/ → package (folder)

### math_utils.py → module

### string_utils.py → module

### __init__.py → tells Python this folder is a package

# 🔍 Why Python needs __init__.py
'''
Python looks at folders in two ways:

📁 Normal folder (just files)

📦 Package folder (importable code)

🔴 Without __init__.py

Python may treat the folder as just a normal directory, not something you can import from (especially in older versions and many environments).

✅ With __init__.py

Python clearly understands:

“This folder contains Python code that can be imported.”
'''

'''
🧪 Simple Example (Very Clear)

Folder structure:
utils/
├── math_utils.py

Try importing:
from utils.math_utils import add


👉 This may fail or behave inconsistently.

Now add __init__.py
utils/
├── __init__.py
├── math_utils.py


Now Python says:

“Okay, utils is a package.”

Import works cleanly.

🧠 Historical (But Important) Reason

Before Python 3.3:

__init__.py was mandatory

Without it → imports fail

After Python 3.3:

Python introduced namespace packages

But:

many tools

many frameworks

interviews

best practices
still expect __init__.py

👉 So always use it as a beginner.
'''

#####  A package is a directory that contains multiple Python modules and an __init__.py file, used to organize related code logically  ####


