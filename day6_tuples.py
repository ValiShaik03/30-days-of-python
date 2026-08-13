# Tuples

## A tuple is exactly like a list, but with one important difference:
## Tuples are immutable, meaning once created, their elements cannot be changed, added, or removed.

# Meaning :
## ❌ We cannot Change 
## ❌ We cannot Add
## ❌ We cannot Remove
## ❌ We cannot update elements
## ✅ We can only access elements

# Tuples are fixed once created

# Tuple Example:
numbers = (10,20,30,40)
# Tuples are round brackets () instead of square brackets
print(numbers)

##### Why do we need tuples if we have lists?
### Tuples are used when :
## Data should NOT change
## For safety
## For faster performance
## For storing permanent values (like days of the week, months etc)

#Examples:
## Months of the year
## Days of the week
## Latitude/Longitude coordinates
## Database rows

# 2. Creating Tuples
# Normal tuple :
colors = ("red","green","blue")

#Tuples with mixed data types
data = ("Shaik",22,True,5.7)

### IMPORTANT : Single-Value Tuple
x = (5) #  ❌ Not a tuple

# Python sees 5 as just a number

## Correct Tuple with single value

y = (5,) # ✅ This is a tuple

## Comma makes  it a tuple

# 3. Accessing Tuple Items (Same as lists)

print(numbers[0]) #10
print(numbers[-1]) #40
print(numbers[1:3]) # 20,30

# What happen when we use double colon :: in slicing ?
print(numbers[1::2]) # here step is 2, so it will take every 2nd element starting from index 1 therefore output is (20,40)

# 4. Trying to modify a tuple (NOT ALLOWED)
#numbers[2] = 50 # This will raise an error
#print(numbers)
#TypeError: 'tuple' object does not support item assignment

#5. Tuple Methods
'''
| Method           | Meaning                     |
| ---------------- | --------------------------- |
| `.count(value)`  | Count occurrences of value  |
| `.index(value)`  | Find index of first value   |
'''
# Tuples only allow two methods:
nums = (1,2,3,4,2,5,4)
print(nums.count(2))

print(nums.index(4))

# 6. Loop through a tuple

names = ("Shaik","vali","prasad","sai","madhav")
for name in names:
    print(name)


#7. Tuple Packing and Unpacking
# Packing
person = ("Shaik",22,"Engineer")
# Unpacking
name, age, profession = person
print(name)
print(age)
print(profession)
# Output:
# Shaik
# 22
# Engineer
# Note : Number of variables on left side must match number of values in the tuple on right side
# Otherwise, it will raise a ValueError

#8. Joining Tuples
tuple1 = (1,2,3)
tuple2 = (4,5,6)
joined_tuple = tuple1 + tuple2
print(joined_tuple) # (1,2,3,4,5,6)
# Note : This creates a new tuple, original tuples remain unchanged

# 9. Coverting Between Lists and Tuples
# Sometimes we need to change a tuple -->list-->modify-->back to tuple

nums1 = (10,20,30)

# Convert tuple to list

temp = list(nums1)
temp.append(40) # Modify list

# Convert list to tuple
nums1 = tuple(temp)
print(nums1)


# Exercise 1:

best_friends = ("Afiya","anjum","lucky","danusree","afifa")
print(best_friends[0]) #Afiya
print(best_friends[-1]) #afifa
print(best_friends[2]) #lucky

# Exercise 2:
numbers2 = (2,4,6,8,20,4,3,6,8)
print(numbers2.count(4)) #2
print(numbers2.index(20)) #4

# Exercise 3:
my_tuple = (10,20,30)
#my_tuple[1] = 30

# Here we are using try-except block to display the error

try:
    my_tuple[1] = 30
except TypeError:
    print("Tuples are immutable!")

# Exercise 4:

data = ("Shaik",22,"India")

temp = list(data)
temp.append("Python")

data = tuple(temp)
print(data)