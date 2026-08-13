# Loops
## A loop is used to repeat a block of code multiple times
## Instead of writing the same code again and again, we use loops

# Why loops are IMPORTANT?
## Loops help you:
### Process lists
### Read files line by line
### Repeat tasks
### Automate work
### Solve interview problems

# No loops = no real programs

# Types of loops in python
## Python has 2 main loops:
### while loop
### for loop

# while loop

## Syntax:
'''
while condition:
    code
'''
# Meaning:
### Keep running the code as long as the condition is TRUE

# Example:
count = 1
while count <= 5:
    print(count)
    count += 1
'''
Output:
1
2
3
4
5
'''
# If condition never becomes False --> Infinite loop

# Example 2:
password =""
while password != "python":
    password = input("Enter password: ")
print("Access granted")

# Infinite Loop
#while True:
    #print("Hello")
# ⚠️ This runs forever unless you stop it.

#Used when:

## waiting for user input

## servers

## games

# for loop
# Syntax:
'''
for variable in sequence:
    Code
'''

# Example 1:(List)

fruits = ["apple","banana","mango"]
for fruit in fruits:
    print(fruit)

# Example 2:(range())
for i in range(5):
    print(i)

# range(start,stop,step)
for i in range(1,10,2):
    print(i)

# Loop Control Statements
## break
### Stops the loop completely
for i in range(10):
    if i == 5:
        break
    print(i)

## continue
### Skips the current iteration
for i in range(5):
    if i == 2:
        continue # it will not print 2 
    print(i)

## pass
### Does nothing (just a placeholder)
for i in range(5):
    pass
## Used when:
### Writing structure first
### Code later

# Nested Loops
## A loop inside another loop

for i in range(3):
    for j in range(2):
        print(i,j)

#### ** Inner loop finishes all its iterations for each single iteration of the outer loop ** ####
                  ## (OR) ##
#### ** The inner loop runs completely for each value of the outer loop ** ####

'''
🧠 Step-by-step Execution (Dry Run)
🟦 First outer loop iteration

i = 0

Now inner loop runs fully:

j = 0 → print(0, 0)

j = 1 → print(0, 1)

🟦 Second outer loop iteration

i = 1

Inner loop again:

j = 0 → print(1, 0)

j = 1 → print(1, 1)

🟦 Third outer loop iteration

i = 2

Inner loop again:

j = 0 → print(2, 0)

j = 1 → print(2, 1)
'''
## Nested Loops are used in:
### patterns
### matrices
### combinations

# Loop with if

numbers = [1,2,3,4,5]
for n in numbers:
    if n % 2 == 0:
        print(n,"is even")

## Exercise Problems ##

# Exercise 1:

## Print numbers from 1 to 10 using while.

count = 1
while count <= 10:
    print(count)
    count += 1

# Exercise 2:
# Print numbers from 10 to 1 using for

for i in range(10,0,-1):
    print(i)

# Exercise 3:
# Print all even numbers from 1 to 20

for i in range(1,21):
    if i % 2 == 0:
        print(i)


# Exercise 4:
# Ask a user to enter 5 numbers and store them in a list using a loop
list1 = []
for i in range(5):
    user = int(input("Enter 5 numbers: "))
    list1.append(user)
print(list1)


# Exercise 5:
# From a list, print only numbers greater than 10
list2 = [12,6,4,2,10,30]
for l in list2:
    if l >= 10:
        print(l)

# Exercise 6:
# Use break to stop loop when number 7 is found
for i in range(10):
    if i == 7:
        break
    print(i)

# Exercise 7:
# Use continue to skipp number 5
for i in range(7):
    if i == 5:
        continue
    print(i)

# Exercise 8:
for i in range(5):
    for j in range(i + 1):
        print("*",end="")
    print()

# for i in range(5):
#     for j in range(5-i):
#         print("*",end="")
#     print()

# for i in range(7):
#     for j in range(i+1):
#         if i == 4:
#             print("*",end="")
#         print()

# for i in range(4):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()

for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print("*",end="")
    print()

##########   Conditions ################
# Conditions decide which code should run and which should not

# Why do we need conditions?
'''
Real life examples:

   If it rains → take umbrella

   If marks ≥ 35 → pass

   If password is correct → login

👉 Programs also need to make decisions.
'''

# if statement(basic)
## Syntax:
# if condition:
#     code

# Example
age = 18
if age >= 18:
    print("Eligible to vote")
# Runs only if condition is True

# if-else
# if condition:
#     code_if_true
# else:
#     code_if_false

# Example
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# if-elif-else
## Used when there are multiple conditions

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# Conditions with comparison operators
'''
| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | equal            |
| `!=`     | not equal        |
| `>`      | greater          |
| `<`      | smaller          |
| `>=`     | greater or equal |
| `<=`     | smaller or equal |

'''

# Logical Operators 

## and ##
country = "America"
if age >= 18 and country == "India":
    print("Eligible")

## or ##
# day = "Monday"
# if day == "Saturday" or day == "Sunday":
# Any one true

## not ##
# if not logged_in:
### Reverses condition

# Nested conditions (if inside if)
age = 20
country = "India"
if age >= 18:
    if country == "India":
        print("Eligible to vote")


# Conditions inside loops 

for i in range(10):
    if i % 2 == 0:
        print(i)

# pass in conditions

if age > 18:
    pass
else:
    print("Minor")
