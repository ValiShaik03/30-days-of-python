# Exercise 1:
'''
Task:

Create a file named math_ops.py

Inside it, define:

   add(a, b)

   sub(a, b)

Each function should return the result
'''

# Exercise 2:
'''
Create another file main.py

Import math_ops

Call both functions and print the results.

👉 Use:

import math_ops
'''

# Exercise 3:
'''
In main.py, import only the add function

Call it without using the module name

👉 Use:

from math_ops import add
'''

# Exercise 4:
'''
Import math_ops using an alias mo

Call both functions using the alias

👉 Use:

import math_ops as mo
'''

# Exercise 5:
'''
Import the built-in math module

Print:

   square root of 25

   value of π

Import the built-in random module

Print a random number between 1 and 10
'''

# Exercise 6
'''
In math_ops.py, add:

if __name__ == "__main__":
    print("math_ops module is running directly")


Run:

    math_ops.py directly

    main.py

👉 Observe:

    When the message prints

    When it does not
'''

# Exercise 7
'''
Create this folder structure:

project/
│
├── main.py
└── utils/
    ├── __init__.py
    └── string_utils.py
'''

# Exercise 10
'''
1. Inside utils/__init__.py, write:

   print("Utils package loaded")

2. Import utils in main.py

3. Observe when this message prints
'''

# Exercise 11
'''
1. Modify utils/__init__.py to expose to_upper

2. So you can do this in main.py:

     from utils import to_upper
'''

# Exercise 12
'''
1. Rename string_utils.py to random.py

2. Try importing Python’s built-in random

3. Observe what breaks

4. Rename it back

👉 Understand why naming conflicts matter
'''