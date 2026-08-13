# Today we'll learn how Python stores data permanently in a database and how real applications do CRUD operations

## 1. What is a Database?
### A database is a structured place to store data permanently so it can be searched, updated, and managed efficiently.

# File vs Database

'''
| File (txt / json / csv) | Database           |
| ----------------------- | ------------------ |
| Simple storage          | Structured storage |
| Hard to search          | Easy to query      |
| No relations            | Supports relations |
| Not scalable            | Scalable           |

'''
# Databases are used when data grows or needs frequent updates

## 2. Why SQLite?
### SQLite is a lightweight database that comes built-in with Python.
#### No installation needed
#### Stored as a single .db file
#### Perfect for learning & small apps


## 3. Connecting Python to SQLite

import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Here :
## connect() --> creates/opens database file
## cursor() ---> used to execute SQL commands
## A cursor is required to execute SQL commands and fetch results.
## Without a cursor, we cannot properly interact with the database.
'''
Database work in Python ALWAYS follows:
connect → cursor → execute → fetch → commit → close
'''

## 4. Creating a Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    age INTEGER,
    marks INTEGER)
""")
conn.commit()

## 5. CRUD Operations
# CREATE (Insert data)
students = [
    ("Shaik",25,88),
    ("Afiya",23,92)
]
cursor.executemany(
    "INSERT INTO students (name,age,marks) VALUES (?,?,?)", students )
conn.commit()

cursor.execute(
    "INSERT INTO students (name,age,marks) VALUES (?,?,?)",("Afiya",5,90)
)
conn.commit()

cursor.execute(
    "INSERT INTO students (name,age,marks) VALUES (?,?,?)",("Mukesh",22,50)
)
conn.commit()

cursor.execute(
    "INSERT INTO STUDENTS (name,age,marks) VALUES (?,?,?)",("Mukesh",22,78)
)
conn.commit()
## We use ? in CREATE (INSERT) operations to safely insert data into the database and avoid security risks like SQL injection
## SQL injection is hacking technique where a user tricks our SQL query into running malicious SQL code
## User input becomes SQL code, not data.

### WITHOUT '?'
# name = input("Enter name: ")

# query = f"SELECT * FROM users WHERE name = '{name}'"
# cursor.execute(query)

# LOOKS NORMAL BUT VERY DANGEROUS BECAUSE THE ABOVE INPUT IS NOT BE TREATED AS DATA IT IS TREATED AS SQL QUERY SO ANYONE CAN ERASE,MODIFY THE ABOVE DATA SO WE SHOULD USE ? IN SQL LITE TO PREVENT SQL INJECTION ATTACKS FROM HACKERS

## READ (Fetch Data)

cursor.execute("SELECT * FROM STUDENTS")
rows = cursor.fetchall()
for row in rows:
    print(row)


## UPDATE (Modify Data)
cursor.execute(
    "UPDATE STUDENTS SET MARKS = ? WHERE name = ?",(100,"AMINA")
)
conn.commit()


'''
UPDATE works ONLY if WHERE condition matches
SQLite string match is CASE-SENSITIVE
Always verify with SELECT + rowcount
'''

## DELETE ( Remove Data)

cursor.execute(
    "DELETE FROM students WHERE name = ?",("Vali",)
)
conn.commit()

conn.close() # To avoid data corruption we must close the database means data should remain unusable,unreadable and even completely inaccessible if we wont close database

