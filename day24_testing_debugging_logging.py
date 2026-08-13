############## Testing, Debugging & Logging #############
# 1. Why Testing Is IMPORTANT?
## Testing answers one question:
### "Is my code correct now and will it stay correct later"

# Without testing:
## Small changes break old code
## Bugs reach users
## Debugging becomes painful

# With testing:
## Confidence
## Faster changes
## Fewer bugs

# 2. Manual Testing vs Automated Testing
## Manual Testing
def add(a,b):
    return a + b
print(add(2,3))
print(add(5,7))

# Problems
## Time-consuming
## Easy to forget cases
## Not repeatable

## Automated Testing
assert add(2,3) == 5
assert add(5,7) == 12

# Benefits
## Runs in seconds
## Repeatable
## Catches regressions (a set of statistical machine learning techniques used to model and analyze the relationship between a dependent variable (the target) and one or more independent variables(predictors or features))

# 3. Assertions (Foundation of Testing)
## What is assert ?
### A statement that checks a condition and fails if its false

def add(a,b):
    return a + b
assert add(2,3) == 5
assert add(1,1) == 2

# If assertion fails : AssertionError

### Assertions are the building blocks of tests

# 4. unittest -- Python's Testing Framework
## unittest is a tool that checks whether our functions are working correctly -- automatically
### Why do we need unittest when we already have assert?

#### assert problem:

## Stops program at first failure
## Not organized
## Not scalable for big problems

#### unittest solution:

## Groups tests properly
## Runs many tests together
## Shows clear report
## Used in real projects
### unittest = structure + professional testing

# Basic Structure of unittest
## Every unittest program has 4 parts:
### Function to test
### Test class (inherits from unittest.TestCase)
### Test methods(start with test_)
### unittest.main()

# 1. Function to test (normal function)
# def add(a,b):
#     return a + b
# # This is our actual code

# # 2. Import unittest
# import unittest
# # This gives Python testing powers

# # 3. Create a Test Class
# class TestAdd(unittest.TestCase):
#     pass
# # This class is only for testing
# # unittest.TestCase gives testing methods

# # 4. Write test methods
# class TestAdd(unittest.TestCase):
#     def test_addition(self):
#         self.assertEqual(add(2,3),5)

# # 5. Run the tests
# if __name__ == "__main__":
#     unittest.main()

# This line tells Python:
## " Run all tests in this file"

# import unittest

# def add(a, b):
#     return a + b

# class TestAdd(unittest.TestCase):
#     def test_add_positive(self):
#         self.assertEqual(add(2, 3), 8)

#     def test_add_zero(self):
#         self.assertEqual(add(0, 0), 0)

# if __name__ == "__main__":
#     unittest.main()

# .. 2 dots means 2 tests passed
# OK --> all tests passed

# If first method is pass and second is failed then we can see .F

# # Basic structure
# import unittest
# def add(a,b):
#     return a + b
# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2,3),5)
#         self.assertEqual(add(1,1),2)
# if __name__=="__main__":
#     unittest.main()

# unitest tells:
## Which test failed
## What was expected
## What actually happened

# Most Common unitest Assertions 
'''
self.assertEqual(a,b) # a == b
self.assertTrue(condition)
self.assertFalse(condition)
self.assertRaises(Error,func)
'''

# Example : Checking Error
# import unittest
# def divide(a,b):
#     return a / b
# class TestDivide(unittest.TestCase):
#     def test_divide_by_zero(self):
#         self.assertRaises(ZeroDivisionError,divide,10,0)
# if __name__ =="__main__":
#     unittest.main()

# unittest is Python's built-in framework to automatically test code in a structured and professional way


# 5. Debugging Mindset
## Golden rule:
### Don't guess -- inspect

# Step-by-step debugging:
## Read the error message
## Identify the line number
## Print intermediate values
## Reduce the problem
## Fix --> test again

# 6. Logging -- Better than print()
## Logging is a way to record what our program is doing while it runs

# Think of logging as a diary or CCTV camera for our program 
## It keeps notes like:
### What happened
### When it happened
### Whether it was normal or an error

# Why not just use print()?
## Using print()
print("User logged in")
print("Error occured")
# Problems
## Cannot turn it ON/OFF easily
## No severity(normal vs error look same)
## Messy in large programs
## Not professional

# Using logging
import logging
logging.info("User logged in")
logging.error("Error occured")

# Benefits:
## Different levels
## Can save logs to a file
## Can disable logs in production
## Used in real projects


# Logging Levels
## Python logging has levels, like importance levels

'''
DEBUG    → detailed info (developer)
INFO     → normal info
WARNING  → something unusual
ERROR    → something failed
CRITICAL → program may crash

'''
# From lowest to highest seriousness

# Simple logging example
import logging
logging.basicConfig(level=logging.INFO,force=True)

logging.info("Program Started")
logging.warning("Low memory")
logging.error("File not found")
#logging.critical("Payment is deducting while entering atm card")

'''
INFO logs were not visible because logging was already configured earlier;
basicConfig() was ignored. Using force=True resets the configuration.
'''

import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    if b == 0:
        logging.error("Division by zero")
        return None
    return a / b

divide(10, 2)
divide(10, 0)

'''
🧠 Why logging is VERY important in real life

Imagine:

App running on server

No screen

Users report “app is slow”

You check logs:

# WARNING : Slow database query
# ERROR : API timeout

## Logs help us debug without seeing the user

'''


'''
Logging is used to track program execution and errors in a controlled,
professional way instead of using print statements.
'''