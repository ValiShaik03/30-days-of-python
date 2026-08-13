# Sets
## A set is a collection that is:
# Unordered (no indexing)
# Unchangeable in terms of items (but the set itself is mutable)
# No duplicate values allowed
# Fast for checking membership (in)

my_set = {1,2,3,4}

'''
4️⃣ Simple real-life analogy 🧠 for set itself is a mutable

Think of a bag of balls:

❌ You cannot change a red ball into a blue ball

✅ You can remove a ball

✅ You can add a new ball

👉 Balls = set items (unchangeable)
👉 Bag = set itself (mutable)
'''

# Key Differences Between Set and List
'''
| Feature            | List         | Set                       |
| ------------------ | ------------ | ------------------------- |
| Duplicates allowed | ✔ Yes        | ❌ No                      |
| Order preserved    | ✔ Yes        | ❌ No                      |
| Indexing           | ✔ Yes        | ❌ No                      |
| Use case           | Ordered data | Unique items, fast lookup |
'''

## Unique Feature
#❌ Duplicates are automatically removed:

s = {1,2,2,3,3,3,4}
print(s) #output : {1,2,3}

# 1. Sets cannot be indexed

s1 = {10,20,30}
#print(s1[0]) # Error : no indexing

# But we can loop through them:
for item in s1:
    print(item)

# 2. Adding and Removing Items
# Add one item:
s2 = {1,2,3}
s2.add(4)
print(s2)

# Add multiple items:
s2.update([5,6,7])
print(s2)

# Remove item (throws error if not found):

s2.remove(3)
print(s2)

# Remove item safely:
s2.discard(8)
print(s2)

# Remove and return random item:
s2.pop()
print(s2)
# Since sets are unordered, .pop() removes a random element (not the first)

# 3. Set Operations 
## Sets support mathematical operations like union, intersection, difference

a = {1,2,3}
b = {3,4,5}

# Union (combine values)

print("Union is : ",a.union(b)) 

# Intersection (Common Values)

print("Intersection is : ",a.intersection(b))

# Difference (in A but not in B)

print("Difference is: ",a.difference(b))

# Symmetrical Difference (not common)
print("Symmetrical Difference is :",a.symmetric_difference(b))

# 4. Convert Between List <--> Set
## Remove duplicates from a list:

nums = [1,1,2,3,3,4,4]
unique_nums = list(set(nums))
print(unique_nums)

# Exercise 1 :

colors = {"red","blue","green","red","yellow"}

print("Here duplicates will be removed and it will given unique values:",colors)

colors.add("black")
print("Black is Added:",colors)
colors.remove("blue")
print("Blue is Removed:",colors)
print(colors)

# Exercise 2 :
a = {1,2,3,4}
b = {3,4,5,6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Exercise 3 :
nums4 = [1,2,2,3,4,4,5]
conversion = list(set(nums4))
print(conversion)

# Exercise 4 :
user = set()
for i in range(5):
    user1 = int(input("Enter 5 numbers:"))
    user.add(user1)
print("My set is:",user)
if 3 in user:
    print("3 is in the set")
else:
    print("3 is not there in the users set")
