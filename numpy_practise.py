# NumPy (Numerical Python) is a Python library used to work with numbers, arrays, and mathematical operations efficiently.
## Why not use Python lists?
'''
Python List	                   NumPy Array
Slow for large data	            Very fast
Stores mixed data types	        Stores same data type
No built‑in math operations	    Powerful math functions
'''

# Real-life Analogy
'''
Python List (The Grocery Store): A list is like a giant supermarket. You can
have soap, milk, and electronics all in one place (Heterogeneous). Because
items are different, the store is huge, and you have to walk around a lot to
find things (Non-Contiguous Memory).

NumPy Array (The Medical Shop): A NumPy array is like a specialised
pharmacy. Everything is a medicine (Homogeneous), and they are packed
tightly in numbered drawers in a specific order (Contiguous Memory). You
can find exactly what you need instantly.

'''
# 2. NumPy Array
## A NumPy array is a collection of values:
### Stored in continuous memory
### All elements have the same data type

import numpy as np
arr = np.array([10,20,30,40])
print(arr)
print(arr.dtype)

# What happens if we mix datatypes in NumPy array?(arr = np.array([10,20,30,40,"a"]))
## NumPy upcasts all elements to a common compatible type (usually string).
## So better we can use list without numpy becoz numpy is designed only for numerical operations

# 3. Types of NumPy Arrays
## 1D Array(One Dimension)
### [10,20,30]
#### Like a single row of data

## 2D Array(Two Dimensions)
'''
[[1,2,3],
 [4,5,6]]
'''
# Like a table (rows & columns)
import numpy as np
arr1 = np.array([[1,2,3],
                 [4,5,6]])
print(arr1)

## 3D Array
### Used in images, videos, deep learning
import numpy as np
arr1 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(arr1)

arr2 = np.array([[[[1]]]])
print(arr2)

'''
NumPy supports 1-dimensional, 2-dimensional, 3-dimensional and n-dimensional arrays with different data types and creation methods.
'''

# 4. Array Creation Methods
## np.array()
### Creates array from list/tuple
arr3 = np.array([1,2,3])
print(arr3)

## np.zeros()
### Creates array filled with 0
arr4 = np.zeros(5)
print(arr4)
# Used when initializing empty data

## np.ones()
### Creates array filled with 1
arr5 = np.ones(3)
print(arr5)

## np.arange()
### Creates numbers with step size
arr6 = np.arange(1,10,2)
print(arr6)

## np.linspace()
### Creates equal spaced values
arr7 = np.linspace(1,10,5)
print(arr7)

#### arange ---> step based
#### linspace -> count based if we give count as 6 and starting as 1 and ending as 10 then it will create 6 equal counts from 1 to 10

# 5. Array Properties
## ndim (Number of Dimensions)
a = arr3.ndim # It will whether it is 1D, 2D, 3D
print(a)

## shape(Rows,columns)
b = arr.shape
print(b)

## size (Total elements)
c = arr1.size
print(c)

## dtype(Data type)
d = arr1.dtype
print(d)
'''
arr1 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
'''
# 6. Indexing and Slicing
## Indexing (Access single value)
e = arr1[0]
print(e)

print("#############")
h = arr1.shape
print(h)
## Slicing (Access range of values)
f = arr1[0:2] # [which block : which row : which column] if we didnt specify block number then it will assume all blocks
print(f)

## 2D Indexing
g = arr1[1,0]
print(g)


# 7. Reshaping Arrays
## reshape()
### Changes shape without changing data
i = arr.reshape(2,2)
print(i)
# Rule : total elements must match
print("## 8 ##")
'''
arr1 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
'''
# 8. Mathematical Operations (Vectorization)
## Element-wise operations
bb = arr1 + 10
print(bb)

cc = arr1 * 2
print(cc)

arr11 = np.array([[1,2],[3,4]])
arr12 = np.array([[5,6],[7,8]])
print(arr11)
print(arr12)
## Array-to-array operations
dd = arr11 + arr12
print(dd)

# 9. Statistical Functions
## Sum
ee = arr11.sum()
print(ee)
## Mean
ff = arr11.mean()
print(ff)
## Min/Max
gg = arr11.min()
hh = arr11.max()
print(gg)
print(hh)
## Standard Deviation
ii = arr11.std()
print(ii)  

# 10. Boolean Indexing (Filtering Data) # Select only values that satisfy condition here I have given arr11 > 2 then it printed 3,4 as output in arr11 we have 1,2,3,4 elements
a1 = arr11[arr11 > 2]
print(a1)
## Used in:
### Data Cleaning
### Removing outliers

# 11. Type Conversion (astype)
a2 = arr11.astype(float)
print(a2)
## Used when:
### Reading CSV files
### Cleaning files

# 12. Copy vs View 
arr11[0] = 222
print(arr11)
# here we can see that at 0th index value is changed, but when we printed our original array it won't affect but in view we can see that affect if we change at any index our original array will also changes and no new memory is created
# and copy is just used to create a same data with new memory here our original array doesn't change
## View
b = arr11.view()
b[0] = 100
print(arr11) # here we can see that our original array is changed i.e. view shares data and no new memory is created

c = arr11.copy()
c[0] = 101
print(arr11) # here we can see the old array only even we try to modify it, but it doesn't because copy doesn't change the original array but it creates the new memory

# How to check
d = b.base is arr11   # True → view
e = c.base is arr11   # False → copy
print(d)
print(e)

## When to Use What?
### Use view() when:
#### We want fast operations
#### We are okay with shared data

### Use copy() when:
#### We don't want original data to change
#### Data safety is important 

######### 📱 Real-Life Analogy: Phone Gallery vs Screenshot ##############
'''
📸 Original Photo = Original NumPy array
👁️ VIEW = Same photo, opened in another app

You open the same photo in:

Gallery app

WhatsApp preview

If you edit the photo (crop / draw)

The photo is changed everywhere

👉 Because it’s the same photo file

📌 This is view()

No new photo created

Same memory

Change in one → change everywhere

🖼️ COPY = Screenshot of the photo

You take a screenshot

Edit the screenshot (draw, crop, write)

Original photo remains unchanged

👉 Screenshot is a new image

📌 This is copy()

New memory

Independent

Changes do NOT affect original

🧠 One-line takeaway (easy to say to anyone):

View = same photo opened twice
'''

# 13. Broadcasting
z = arr11 + 5
print(z)
## can we say broadcasting is same as element-wise operation
### Answer
'''
❌ Broadcasting is not element-wise operation
✅ Broadcasting is what allows element-wise operation when shapes differ

# 1️⃣ What is an Element-wise Operation?

Element-wise operation means:

Each element in one array operates with the corresponding element in another array.

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b

What happens:
1+10, 2+20, 3+30
📌 This is pure element-wise operation
📌 Both arrays already have the same shape

# 2️⃣ What is Broadcasting?

Broadcasting happens before element-wise operation.

Broadcasting adjusts the shape of smaller data so that element-wise operation becomes possible.

Example:
a = np.array([1, 2, 3])
a + 5

What NumPy does internally:
[1 2 3]
+ [5 5 5]   ← broadcasting
-----------
[6 7 8]     ← element-wise operation

🔹 Broadcasting makes element-wise operations possible when shapes are different

📌 5 is NOT element-wise by itself
📌 It becomes element-wise only after broadcasting
'''

#### Real-Life Analogy
'''
Analogy: Teacher Giving Bonus Marks

There are 3 students:

[10, 20, 30]  ← marks


Teacher says:

“Add 5 bonus marks to everyone”

Teacher does NOT say:

[5, 5, 5]


But automatically:

10+5, 20+5, 30+5


📌 The same bonus is applied to all students

👉 This is broadcasting
'''

# 14. Conditional Operations
## np.where()
oo = np.where(arr11 > 50, "Pass","Fail")
print(oo)
# Used for decision-making

# 15. Random Numbers
## Random floats
ss = np.random.rand(5)
print(ss)
## Random integers
pp = np.random.randint(1,100,10)
print(pp)
# Used in:
## Sampling
## ML datasets

# 16. NumPy in Real Life
'''
Field	                Usage
Data Analysis	    Fast calculations
Machine Learning	Model input data
Image Processing	Pixel manipulation
Finance	            Risk & return
'''

#### NumPy allows us to store data efficiently, process it fast, and perform complex math easily, making it the backbone of Data Science