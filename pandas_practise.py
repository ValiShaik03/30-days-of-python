# 1. What is Pandas ?
## Pandas is a Python library used to:
### Work with table-like data
### Read data from files(CSV, Excel, JSON)
### Clean, filter, analyze data
### Perform fast calculations
# Pandas is like a Excel inside Python (but more powerful)

# 2. Why do we need Pandas?
## Before Pandas:

### Lists
### Dictionaries
### Loops
### Manual Calculations

## With Pandas:

### One line operations
### Cleaner code
### Faster analysis

# 3. Core Pandas Data Structures
## 1. Series (1D data)
### Like a single column
## 2. DataFrame (2D data)
### Like a table (rows + columns)

# 4. Import Pandas
import pandas as pd

# 5. Pandas Series (1D)
import pandas as pd
numbers = pd.Series([10,20,30,40])
print(numbers)
# Left side --> Index
# Right side -> Values

# 6. Custom Index in Series
s = pd.Series([90,85,88], index=["Math","Science","English"])
print(s)
# Index = labels (like keys)

# 7. Access Series Data

print(s["Math"]) # by label
print(s[0])      # by position
print(s["Science"])
# 8. Pandas DataFrame (2D)

# 8. Pandas DataFrame (2D) # DataFrame is simply like a table
## Creating DataFrame from dictionary
data = {
    "Name":["Vali","Shaik","Afiya","B","C","D"],
    "Age":[22,25,23,24,35,67],
    "Marks":[90,88,92,90,88,35],
    "Alphabets":["A","B","C","D","E","F"],
    "Place":["Hyd","Banglr","Chennai","HH","LL","AP"],
    "PinCode":[5233,5234,5235,5236,5237,5238]
}
df = pd.DataFrame(data)
print(df)

# 9. Access Columns
print(df["Name"][0])
print(df["Marks"][0])

# 10. Access Rows
## loc --> select using column name/ row label like # df.loc[1,"Name"] then it will produce output but if we give df.loc[1,0] it will produce error as KeyError because loc is used when we know exact column name it wont be accessed using position like df.loc[1,0]
## iloc -> select using row number/ position like # df.iloc[1,0] then it will produce output without error but if we give like df.iloc[1,"Name"] then it will produce error like location based indexing can only have integer values
# print(df.loc[1,0]) Not possible
print(df.loc[0,"Age"]) # This is possible
# print(df.iloc[1,"Name"]) Not possible
print(df.iloc[1,0]) # Possible

# 11. Basic Data Inspection
c = df.head() # first 5 rows
print(c)
print("tail")
d = df.tail() # last 5 rows
print(d)
e = df.shape # (rows, columns)
print(e) 
f = df.info() # data types + nulls
print(f) 
g = df.columns # column names
print(g)
h = df.describe() # statistics summary
print(h)
# 12. Simple Operations
print(df["Marks"].mean())
print(df["Age"].max())
print(df["Marks"].min())

# 13. Reading CSV Files
## Why CSV?
### Most datasets are in CSV format
### Easy to share & analyze
import pandas as pd
df = pd.read_csv("marks.csv")
print(df.head())
# This loads data into a DataFrame
print(df)

# 14. Filtering Rows
## Filter using condition
i = df[df["marks"] >= 90]
print(i)
## Multiple Conditions
j = df[(df["marks"] > 85) & (df["name"] == "Vali")]
print(j)

'''
👉 Use and when making decisions
👉 Use & when working with data (arrays, columns)
'''
print("15th Concept")
# 15. Selecting Specific Columns
k = df[["name","marks"]]
print(k)

# 16. Add New Column
l = df["Passed"] = df["marks"] >= 40
print(l)
print(df)

# 17. Modify Existing Column
s = df["marks"] = df["marks"] + 5
print(s)

# 18. Drop Columns/Rows
# axis = 1 means it is for column
# axis = 0 means it is for row
# If we doesn't give inplace = True then it will not change our dataframe 
## Drop Column
q = df.drop("Passed",axis = 1, inplace = True)
print(q)
print(df)

## Drop Row

ii = df.drop(0,axis = 0, inplace = True)
print(ii)
print(df)

# 19. Sorting Data
oo = df.sort_values("marks",ascending=False)
print(oo)
print(df)

# 20. Handling Missing Values
## Check missing values
qq = df.isnull().sum()
print(qq)

## Drop missing values
ww = df.dropna()
print(ww)

## Fill missing values
z = df.fillna(0)
print(z)

# 21. GroupBy
y = df.groupby("marks")["age"].mean()
print(y)
## Used for aggregation
## Aggregation means summarizing multiple values into a single value(like sum,average,count,min,max)

# 22 Apply Function
df["Grade"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df)

# 23. Merging DataFrames
## Used when we have related tables (like SQL JOIN)
print("#### Concept 23 ####")
import pandas as pd
df1 = pd.DataFrame({
    "id":[1,2,3,4,5],
    "name":["Vali","Shaik","Afiya","Amina","Shaheen"],
    "age":[23,22,5,7,21]
})
df2 = pd.DataFrame({
    "id":[1,2,3,6,7],
    "marks":[90,88,92,78,84],
    "place":["hyd","cbm","mrkp","ap","banglr"]
})
merged = pd.merge(df1,df2,on="id")
print(merged)
# This is same as SQL INNER JOIN

# 24 Types of Merge
'''
| Type  | Meaning                   |
| ----- | ------------------------- |
| inner | common records            |
| left  | all left + matching right |
| right | all right + matching left |
| outer | all records               |

'''
print("Left Join") # Here we get all data from df1 and only matching data from df2
merged1 = pd.merge(df1,df2,on="id",how="left")
print(merged1)

print("Right Join") # Here we get all data from df2 and only matching data from df1
merged2 = pd.merge(df1,df2,on="id",how="right")
print(merged2)

# 25. Concatenation (Stacking Data)
## Used to add rows or columns

# Row-wise (default)
print("25th Concept")
v = pd.concat([df1,df2])
print(v)

print("Column-wise")
# Column-wise
u = pd.concat([df1,df2], axis = 1)
print(u)

# 26. Save DataFrame to CSV
x = df.to_csv("output.csv",index = False)
print(x)
'''
index=False prevents Pandas from saving the DataFrame’s index as a column in the CSV file
Like in every dataframe we are having 0,1,2,3,.. index values to avoid those values in our csv file we are using index=False
'''
print("Exercises")

# Exercises
##🔸 Exercise 1

### Filter students with marks > 85

io = df[df["marks"] > 85]
print(io)
##🔸 Exercise 2

### Add a column Result (Pass / Fail)

ex = df["Result"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(ex)
##🔸 Exercise 3

### Group by age and find average marks

ey = df.groupby("age")["marks"].mean()
print(ey)
##🔸 Exercise 4

### Sort by marks (descending)

ez = df.sort_values("marks", ascending=False)
print(ez)

########### CHEAT SHEET ###########
'''
import pandas as pd

# Read
pd.read_csv("file.csv")

# Inspect
df.head()
df.info()
df.describe()

# Select
df["col"]
df.loc[0]
df.iloc[0]

# Filter
df[df["col"] > 10]

# Add column
df["new"] = df["col"] * 2

# Drop
df.drop("col", axis=1)

# Sort
df.sort_values("col")

# Group
df.groupby("col").mean()

# Merge
pd.merge(df1, df2, on="id")

# Save
df.to_csv("out.csv", index=False)
'''