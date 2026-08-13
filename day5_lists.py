# Lists
## A list is used to store multiple values in one variable

# Example:
fruits = ["apple","banana","cherry"]

## List can store:
# numbers, strings, boolean, even mixed types

# Example:
mixed = ["Shaik", 22, True, 5.7]

##### Lists are **Ordered** and **Changeable**

### Meaning:
# Ordered Means : Values have index positions
# Changeable : We can modify them anytime

# # 2. Indexing in Lists

# Index starts from 0
print(fruits[0]) # apple
print(fruits[-2]) # banana

# 3. Updating List Items
fruits[2] = "mango"
print(fruits)

# # 4. List Methods
# '''
# | Method                  | Meaning                  |
# | ----------------------- | ------------------------ |
# | `.append()`             | Add item to end          |
# | `.insert(index, value)` | Add at specific position |
# | `.remove(value)`        | Remove specific value    |
# | `.pop()`                | Remove last item         |
# | `.pop(index)`           | Remove by index          |
# | `.sort()`               | Sort ascending           |
# | `.reverse()`            | Reverse list             |
# | `len(list)`             | Count items              |
# '''

numbers = [5,2,8,1]
numbers.append(10)      # Add 10 at end
numbers.insert(1,6) # Add 6 at index 1
numbers.remove(5) # Remove value 5
numbers.pop()        # Remove last item
numbers.pop(1)     # Remove item at index 1
numbers.sort()      # Sort list
numbers.reverse()   # Reverse list
print(numbers) 

# 5. Loop through a list

fruits1 = ["apple","banana","cherry"]

for item in fruits1:
    print(item)


friends = ["Ravi", "Kumar", "Santhosh", "Amit"]
print(friends)
print("First friend:", friends[0])
print("Last friend:", friends[-1])

friends.append("Suresh")
print("After append:", friends)

friends.insert(2, "Rahul")
print("After insert:", friends)

friends.remove("Kumar")
print("After remove:", friends)

# 6. Copying a list

a = [1,2,3]
b = a.copy()
print("list a: ", a)
print("list b {copy of a}:",b)
# Both refer to the same list!

# 7. Nested Lists (Lists inside lists)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1][2])  # Output: 6


# Exercise 1
#Create a list of 5 favorite movies and:
movies = ["RRR", "Baahubali", "KGF", "Dangal"]
print("Movies List:", movies)

#Print the first and last movie
print("First Movie:",movies[0])
print("Last Movie:",movies[3])

#Replace the second movie with another one
movies.insert(1,"Salaar")
print("Replacing Baahubali With:",movies)

#Append one new movie
movies.append("Darling")
print("Adding One New Movie:",movies)

# Exercise 2

num = [10, 50, 30, 70, 20]

print(num)
num.sort()
print("Sorting: ",num)
num.reverse()
print("Reversing the numbers: ", num)
print("Length of the list: ",len(num))


# Exercise 3
## Ask user to enter 5 favorite foods and store them in a list using .append()

foods = []
for i in range(5):
    food = input("Enter your favorite food: ")
    foods.append(food)
print(foods)
# Exercise 4 
##Reverse any list without using .reverse()
list = [5,"abcd",True,88.9]

reversed_list = list[::-1]
print(reversed_list)



# # # We should not do this when using lists

# # # append/insert/sort/reverse return None

# # # Always print the list after modification, not the method

# # # like this :
# # ## movies.insert(1,"Salaar")
# # ## print("Replacing Baahubali With:",movies)

# # # Not like this :
# # ## print(movies.insert(1,"Salaar"))  # Wrong

# # # Because it will print None 

# # # Why it returns None?

# # # To avoid confusion, as the list is modified in place
# # # and the method does not return a new list.
# # # So, printing the method would not show the updated list.
# # # Always print the list variable itself after modification.


# movies2 = ["A", "B", "C"]
# print(movies2.append("D"))  # Wrong
# print("After append:", movies2)  # Correct
# # So we should avoid printing the result of append/insert/sort/reverse methods directly. instead print the list after modification.


# ##############     *********** LISTS ARE MUTABLE MEANS THEY ARE ORDERED AND CHANGEABLE **********   ##############