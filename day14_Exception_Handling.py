# ############### Exception Handling ####################

# # What is an Exception?
# ## An exception is an error that occurs while a program is running
# # Example
# # a = 10/0
# # Output
# ## ZeroDivisionError
# ### Program crashes and stops

# # Why do we need Exception Handling?
# ## Without Exception Handling:
# # Program crashes
# # User sees ugly error messages
# # Program stops suddenly

# ## With Exception Handling:
# # Program continues
# # Error is handled politely
# # User-friendly messages


# # Basic Structure Of Exception Handling
# '''
# try:
#     # risky code
# except:
#     # handle error 
# '''

# # Simple Example 
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except:
#     print("Something went wrong")

# # Catching Specific Exceptions
# # Never use generic except always
# # Handle specific errors

# # Example

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("We cannot divide a number by zero")
# except ValueError:
#     print("Plese enter valid number")

# # Multiple Exceptions Together
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except (ZeroDivisionError, ValueError):
#     print("Invalid input or division by zero")

# # else block
# ## else runs only if NO exception occurs

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("We cannot divide a number by zero")
# else:
#     print("Calculation successful")

# # finally
# ## finally always runs, whether error occurs or not
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
# except Exception as e:
#     print("ZeroDivisionError",e)
# finally:
#     print("Program finished!")

# # Use Case:
# ## Closing files
# ## Closing database connections
# ## Cleanup actions

# # Using Exception as e
# try:
#     x = int("abc")
# except Exception as e:
#     print(e)

# # Output
# ## invalid literal for int() with base 10: 'abc'

# # Raising Custom Exceptions
# ## We can raise our own errors

# age = int(input("Enter age: "))
# if age < 18:
#     raise ValueError("Age must be 18 or above")
# print("You are eligible!")

# # Custom Exception Class
# class InvalidAgeError(Exception):
#     pass
# age = int(input("Enter age: "))
# if age < 18:
#     raise InvalidAgeError("Age below 18 not allowed")


# #### Common Built-in Exceptions ####
# '''
# | Exception           | When it occurs         |
# | ------------------- | ---------------------- |
# | `ZeroDivisionError` | divide by zero         |
# | `ValueError`        | wrong type conversion  |
# | `TypeError`         | wrong data type        |
# | `IndexError`        | invalid index          |
# | `KeyError`          | missing dictionary key |
# | `FileNotFoundError` | file missing           |

# '''


# #### 🎯 One-line Memory Rules ####
# '''
# try → risky code

# except → handle error

# else → runs if no error

# finally → always runs

# raise → create error
# '''

# Exercise Problems
## Exercise 1
# Handle division by zero using try-except.
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("We cannot divide a number by zero")

# # Exercise 2
# # Ask user for a number and handle ValueError
# try:
#     user = int(input("Enter a number: "))
#     print("You entered: ",user)
# except ValueError:
#     print("Wrong Type Converison")

# # Exercise 3:
# #Use try-except-else-finally in one program.
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a/b
# except ZeroDivisionError:
#     print("Cannot Divide By Zero")
# else:
#     print("Result is: ",result)
# finally:
#     print("Program finished!")

# # Exercise 4:
# # Raise an exception if marks < 40.
# marks = int(input("Enter your marks: "))
# if marks < 40:
#     raise ValueError("You are failed!!")
# print("You are pass")


# ######## Day 14 Part-2 ########

# # Custom Exception Classes 
# ## Why do we need custom exceptions?
# # Built-in errors like ValueError are generic
# # Sometimes we want our own meaningful error

# ## Example:
# # "Low Balance", "Invalid Age", "Login Failed"

# # How to Create a Custom Exception
# ## Basic Syntax:
# class MyError(Exception):
#     pass
# # This creates a new exception type

# # Simple Example -- Age Validation
# class InvalidAgeError(Exception):
#     pass
# age = int(input("Enter age: "))
# if age < 18:
#     raise InvalidAgeError("Age must be 18 or above")
# print("Eligible")

# # Output(if age < 18):
# ## InvalidAgeError: Age must be 18 or above
# # This error is clear and meaningful

# # Catching Custom Exceptions
# class InvalidAgeError(Exception):
#     pass
# try:
#     age = int(input("Enter age: "))
#     if age < 18:
#         raise InvalidAgeError("Age below 18 not allowed")
# except InvalidAgeError as e:
#     print(e)

# # ✔ Custom error
# # ✔ Clean handling
# # ✔ User-friendly

# # Real-World Example 1 -- Bank Withdrawal

# class InsufficientBalanceError(Exception):
#     pass
# balance = 5000
# try:
#     amount = int(input("Enter withdraw amount: "))
#     if amount > balance:
#         raise InsufficientBalanceError("Not Enough Balance")
#     balance -= amount
#     print("Withdraw Successful!, Your Current Balance: ",balance)
# except InsufficientBalanceError as e:
#     print(e)

# # Real-World Example 2 -- Login System

# class LoginError(Exception):
#     pass
# try:
#     username = input("Username: ")
#     password = input("Password: ")
#     if username != "admin" or password != "1234":
#         raise LoginError("Invalid login credentials")
#     print("Login Successful")
# except LoginError as e:
#     print(e)


# # Nested try-except
# ## Sometimes one error depends on another
# try:
#     try:
#         num = int(input("Enter number: "))
#         print(10/num)
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input")

## We should use nested only when needed, not always

## Exercise Problems
# Exercise 1
# Create a custom exception NegativeNumberError.
# Raise it if user enters a negative number.

class NegativeNumberError(Exception):
    pass
user = int(input("Enter a number: "))
if user < 0:
    raise NegativeNumberError("This is a negative number")
print("Positive Number")

# Exercise 2
# Write a program to read two numbers and divide them:

# Handle ValueError

# Handle ZeroDivisionError

# Use else and finally

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result is: ",result)
finally:
    print("Program Done!!")


# Exercise 3

class InsufficientLength(Exception):
    pass
try:
    user = input("Enter your password: ")
    if len(user) < 8:
        raise InsufficientLength("Password must be at least 8 characters long")
    print("Password Accepted")
except InsufficientLength as e:
    print(e)

# Key Takeways and Mistakes to Overcome 
'''
1️⃣ Custom exceptions must be raised, not just defined
2️⃣ Passwords should be strings, not integers
3️⃣ len() works on sequences, not numbers
4️⃣ try should wrap risky code only
'''
