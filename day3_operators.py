a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
difference = a - b
product = a * b
division = a / b

print("Sum is : ",sum)
print("Difference is : ",difference)
print("Product is : ",product)
print("Division is : ",division)

# Exercise 2

a1 = int(input("Enter a number: "))

if a1 % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Exercise 3

age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18 and (country == "India" or country == "india"):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Exercise 4

name = input("Enter your name:")
age1 = int(input("Enter your age: "))

future_age = age1 + 5

print(f"Hello {name}, in 5 years you will be  {future_age} years old")

