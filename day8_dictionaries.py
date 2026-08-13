# Dictionaries
## Dictionaries are used everywhere in real-world coding:
### APIs return data as dictionaries
### JSON = dictionary
### Databases return row like dictionaries
### AI & ML configs
### User Profiles
### Settings,options,states
### Key-value storage

# What is a Dictionary?
## A dictionary stores data in key-value pairs.
## Example:
student = {
    "name":"Shaik",
    "age":22,
    "country":"India"
}

# Keys ---> Identifiers
# values --> Data

## Why are dictionaries important?
# Because we can store data in a structured way like:
#name    --->  Shaik
#age     --->  22
#country --->  India
#skill   --->  Python

# Syntax:
my_dict = {
    "key1":"value1",
    "key2":"value2"
}

## Keys must be :
#  **Strings**
#  **Integers**
#  **Tuples**

# Values can be anything:String, int, list, dictionary, etc.

# 1. Accessing Dictionary Values

print(student["name"]) # Shaik
print(student["age"]) # 22

# If key does not exist ----> KeyError

# If we use .get() then we dont get any error if the key is not present instead of error it just passes **None**

print(student.get("email")) # None

# 2. Updating Values
student['age'] = 23
print(student)
# Adding a new key:
student['langugae'] = "Python"
print(student)

# 3. Adding Items
student["hobby"] = "Cricket"
print(student)

# 4. Removing Items

# pop(key)
## Removes specific key:

student.pop("age")
print(student)

# popitem()
## Removes last inserted item:

student.popitem()
print(student)

#del 
##Remove by key:

del student["country"]
print(student)

#clear()
#Remove everything:

student.clear()
print(student)

'''
| Feature                         | pop()  | del     |
| ------------------------------- | ------ | ------- |
| Removes key?                    | ✔ Yes  | ✔ Yes   |
| Returns value?                  | ✔ Yes  | ❌ No    |
| Causes KeyError if key missing? | ✔ Yes  | ✔ Yes   |
| Syntax                          | method | keyword |

'''

student = {
    "name":"Shaik",
    "age":22,
    "country":"India"
}

# 5. Looping through a dictionary

#To get all keys
for key in student:
    print(key)

#To get all values
for value in student.values():
    print(value)

#To get key + value
for key,value in student.items():
    print(key,value)


# 6. Nested Dictionary :

user = {
    "name": "vali",
    "Skills": ["AI","Python","SQL","ML"],
    "details":{
        "age":22,
        "country":"India"
    }
}
print(user["details"]["age"])


### ***** Dictionary is Mutable ***** #######


'''
| Type  | Mutable? | Ordered? | Duplicate keys? | Access by   |
| ----- | -------- | -------- | --------------- | ----------- |
| List  | Yes      | Yes      | Yes             | index       |
| Tuple | No       | Yes      | Yes             | index       |
| Set   | Yes      | No       | No              | no indexing |
| Dict  | Yes      | Yes      | No              | key         |

'''

# Exercise 1 :

profile = {
    "name": "Shaik",
    "age": 22,
    "city": "Hyderabad",
    "skills": ["Python", "AI"]
}
print(profile["name"])
print(profile["age"])
print(profile["skills"])
print(profile["skills"][1])

# Exercise 2 :

profile["country"] = "India"
profile["experience"] = "Fresher"

profile["age"] = 23
print(profile)

# Exercise 3
profile.pop("city")
del profile["skills"]
print(profile)

#Exercise 4
for key in profile:
    print(key)

for value in profile.values():
    print(value)

for key, value in profile.items():
    print(key,value)


# Exercise 5:
student1 = {
    "name": "Shaik",
    "education": {
        "10th": 9.7,
        "12th": 9.4,
        "degree": 8.0
    }
}
print(student1["education"]["12th"])