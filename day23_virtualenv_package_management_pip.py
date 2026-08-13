### Virtual Environments & Package Management (pip)
# Today we will learn how professionals manage Python projects without breaking anything
# Until now, we ran Python globally
# From today, we will run Python project-by-project like real developers
# Problems this solves:
## It works on my machine but not yours
## Package version conflicts
## Breaking old projects when installing new libraries


# 1. What is a Virtual Environment ?
## A virtual environment is an isolated Python space for one project.
### One project --> one Python world

# Without virtual environment
## Project A needs Django 3
## Project B needs Django 5
### When we install Django 5 --> Project A breaks

# With virtual environment
## Project A --> venv --> Django 3
## Project B --> venv --> Django 5
### No conflicts

# Real-life analogy
## Global Python = One kitchen for all recipes
## Virtual env = One kitchen per recipe

# 2. Creating a Virtual Environment
## Step 1: Go to your project folder
# cd MyProject
## Step 2: Create venv
# python -m venv venv
## This creates:
'''
MyProject/
│
├─ venv/
'''

# 3. Activating the Virtual Environment
## Windows
### venv\Scripts\activate
## Mac / Linux
### source venv/bin/activate

# We will see
## (venv) at the beginning of the terminal --> That means it is activated
# Important Rule
# Always activate venv before installing packages

# 4. What is pip ?
## pip is Python's package installer
# Example:
# pip install requests
# Install the requests library inside the active virtual environment
#  Check installed packages:
# pip list

# 5. Freezing Dependencies
# Why ?
## So others can install exact same packages & versions
### Create requirements file
# pip freeze > requirements.txt
# File Example:
# requests == 2.31.0
# numpy == 1.26.2

## Install from requirements.txt
# pip install -r requirements.txt
# This is how teams share projects

# 6. Deactivating Virtual Environment
## deactivate
# We'll return to global Python

# 7. One-Glance Workflow
'''
python -m venv venv
venv\Scripts\activate
pip install package_name
pip freeze > requirements.txt
deactivate
'''

'''
I just want to know the main concept 
in freezing dependencies because when I use pip freeze > requirements.txt some extra libraries are installed why?
'''
#### Answer

'''
🔒 Real-world analogy (very simple)

We order Biryani 🍛
We didn’t order:

Rice

Spices

Chicken

Oil

But the restaurant needs all of them.

pip freeze lists all ingredients, not just “Biryani”.
'''

'''
pip freeze captures the complete dependency tree so the project can be 
reproduced exactly on another system.
'''

## Direct Packages & Indirect dependencies
'''
Direct packages (requests, numpy)

Indirect dependencies (urllib3, certifi, etc.)
'''

### SIMPLE DEFINITION ABOUT VIRTUALENV
'''
🧳 Virtualenv = Separate Bags

Imagine you are traveling with multiple trips:

Trip 1 → Winter clothes 🧥

Trip 2 → Summer clothes 👕

If you put all clothes in one bag ❌
→ You get confused, clothes mix, hard to manage.

So what do you do?
👉 Use separate bags for each trip ✅

🧠 How this matches Python

Your computer → House

Python → You

Projects → Trips

Packages (Django, NumPy, etc.) → Clothes

Virtualenv → Separate bags

Each project gets its own bag (virtualenv) with only the packages it needs.

🟢 Final simple line

Virtualenv is like a separate bag for each Python project so nothing gets mixed up.
'''
########### DAY 23 CHEAT SHEET ###########
'''
# ==================================================
# DAY 23 — VIRTUAL ENVIRONMENT & PIP
# ==================================================

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate        # Windows
source venv/bin/activate    # Mac/Linux

# Install packages
pip install package_name

# List installed packages
pip list

# Freeze dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate environment
deactivate

# IMPORTANT NOTES:
# - Always activate venv before installing packages
# - requirements.txt contains ALL dependencies
# - Do NOT commit venv/ folder (add to .gitignore)
# - pip freeze captures exact versions

'''