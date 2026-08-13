############ Regular Expressions (re module) ############

# What is Regex?
## Regex is a way to search, match, or extract patterns from text
## It is used for string searching and manipulation
## Examples of patterns:
### email --> pattern with "@" and "."
### phone number --> patterns with digits and dashes
### only digits --> patterns with 0-9
### only alphabets --> patterns with a-zA-Z
### password rules ---> patterns with length, special characters and digits

# Is Regex works only for text?
## Yes, regex is specially designed for text processing
## It cannot be used for binary data directly

# Why do we need Regex?
## Because text data is everywhere: files, user input, web data ,etc
## Regex helps to validate, search, and manipulate text efficiently
# Without regex:
## Long if conditions
## Manual character checking
## Messy code
# With regex:
## One line
## Powerful apttern matching
## Cleaner code

# Without REGEX (Normal Python)
'''
text = "Hello123"

found_digit = False

for ch in text:
    if ch.isdigit():
        found_digit = True
        break

if found_digit:
    print("Contains digit")
else:
    print("No digit")

'''

# What’s happening?
'''
Loop through every character

Manually check .isdigit()

More lines

More logic
'''

# With REGEX
'''
import re

text = "Hello123"

if re.search(r"\d", text):
    print("Contains digit")
else:
    print("No digit")

'''

# What happened?
'''
\d means “any digit”

search() finds it anywhere

One condition, one line
'''

# Why regex is better here?
'''
✔ Less code
✔ More readable
✔ No manual loop
'''

# Importing Regex Module
import re
# All regex operations come from re module

# Most Important Regex Functions
'''
| Function       | Use                   |
| -------------- | --------------------- |
| `re.search()`  | Find pattern anywhere |
| `re.match()`   | Match from start only |
| `re.findall()` | Find all matches      |
| `re.sub()`     | Replace text          |
'''

# re.search() -- Find pattern anywhere
import re
text = "I am learning Python"
result = re.search("Python",text)
print(result) 
# Output:
# <re.Match object; span=(14, 20), match='Python'>

## If pattern not found ---> None

# Practical Example
if re.search("Python",text):
    print("Word Found")
else:
    print("Not found")

# re.match() -- Match from beginning only
import re
text = "Python is fun"
print(re.match("fun",text))
print(re.match("Python",text))
# Output:
# match() checks ONLY start of string

# re.findall() -- Find all matches
import re
text = "Python is easy. Python is powerful"
result = re.findall("Python",text)
print(result)
# Output:
# ['Python','Python']
# If no matches ---> empty list []

# Character Classes 
'''
| Pattern | Meaning                 |
| ------- | ----------------------- |
| `\d`    | digit (0–9)             |
| `\D`    | not digit               |
| `\w`    | word (a-z, A-Z, 0-9, _) |
| `\W`    | not word                |
| `\s`    | whitespace              |
| `\S`    | not whitespace          |

'''

'''
\d - digit(0-9)
\D - not digit
\w - word(a-z,A-Z,0-9,_)
\w - not word
\s - whitespace
\S - not whitespace
'''

# Example -- find digits
text = "My number is 98765"
print(re.findall("\d",text))
# Output
# ['9','8','7','6','5']

print(re.findall("\D",text))
print(re.findall("\w",text))
print(re.findall("\W",text))
print(re.findall("\s",text))
print(re.findall("\S",text))

# Quantifiers (HOW MANY TIMES)
'''
| Symbol  | Meaning         |
| ------- | --------------- |
| `*`     | 0 or more       |
| `+`     | 1 or more       |
| `?`     | 0 or 1          |
| `{n}`   | exactly n       |
| `{n,m}` | between n and m |

'''
# Example - find 1 or more digits together
text = "My numbers are 98 and 7654"
print(re.findall("\d+",text))
# Output:
# ['98','7654']

# Example - find exactly 2 digits together
print(re.findall("\d{2}",text))
print("############")
# Output:
# ['98','76','54']
text1= "My numbers are 098 and 76545"
print(re.findall("\d+",text1)) # here + means 1 or more digits together so output will be ['098','76545']

print(re.findall("\d*",text1)) # how many times 0 or more digits occurs

print(re.findall("\d?",text1)) # how many times 0 or 1 digit occurs

print(re.findall("\d{1,3}",text1)) # here we are finding digits between 1 and 3 so output will be ['098','765','45'] 



# Example -- Phone Number (10 digits)
pattern = "\d{10}"
text = "My phone is 9876543210"
print(re.search(pattern,text))

#Output
# <re.Match object; span=(12, 22), match='9876543210'>

# Simple Email Check
import re
email = "test@gmail.com"
pattern = "\w+@\w+\.\w+"
if re.search(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")


# re.sub() -- Replace text
import re
text = "I love Java"
new_text = re.sub("Java","Python",text)
print(new_text)

# Exercise Problems
# Exercise 1:
import re
string1 = "My number is 1234567098"
print(re.findall("\d",string1))
if re.search("\d",string1):
    print("Digits Found")
else:
    print("No Digits Found")

# Exercise 2:
string2 = "I have 2 apples and 10 bananas"
print(re.findall("\d+",string2))

# Exercise 3
string3 = "Contact me at 9876543210"
if re.search("\d{10}",string3):
    print("10 digit number found")
else:
    print("10 digit number not found")

# Exercise 4
string4 = "My name is Vali"
print(re.sub(" ","_",string4))

import re
text = "My number is 9876543278"
print(re.findall(r"\d{10}", text))


# Regex Quantifiers Summary
## Quantifiers tell regex how many times to match

# 1. + ---> One or more
## Meaning:  Atleast 1 time, can be more
### Example:
import re
text = "abc12345xyz"
print(re.findall("\d+",text))
# Output: ['12345']
# Explanation: \d+ matches '12345' as it has one or more digits together

# Without +:
print(re.findall("\d",text))
# Output: ['1','2','3','4','5']
# Explanation: \d matches each digit separately

# \d ---> digit by digit
# \d+ --> full number

# 2. * ---> Zero or more
## Meaning: Can appear 0 times or many times
### Example:
import re
text = "abcxyz"
print(re.findall("\d*",text)) # if we give + after \d it will print empty list but if we give * it will print list of empty strings because * means 0 or more and + means1 or more
# Output: ['', '', '', '', '', '', '']
# Explanation: \d* matches zero digits at every position
# There are no digits, so it matches empty strings
# If there were digits, it would match them too

text = "abbbc"
print(re.findall("ab*c",text))
# Output: ['abbbc']
# Explanation: b* matches zero or more 'b's between 'a' and 'c'


# 3. ? ---> Zero or one 
## Meaning: Can appear 0 times or 1 time
### Example:
import re
text = "color colours"
print(re.findall("colou?r",text)) # if we have text like "color colours" and if we give re.findall("colours?",text) then it will print only ['colours'] because ? means 0 or 1 so it will match only once but if we give re.findall("colou?r",text) then it will print both color and colour because u? means 0 or 1 so it will match both
# Output: ['color', 'colour']
# Explanation: u? matches zero or one 'u'

# 4. {n} ---> Exactly n times
## Meaning: Must appear exactly n times
### Example:
text = "aaabbbccc"
print(re.findall("a{3}",text)) # if we give re.findall("a{4}",text) then it will print empty list because there are only 3 a's together but if we give re.findall("a{3}",text) then it will print ['aaa']
# Output: ['aaa']
# Explanation: a{3} matches exactly 3 'a's together
# If there were less or more, it wouldn't match

# 5. {n,m} ---> Between n and m times
## Meaning : Must appear n times not more than m times
### Example:
text = "aaaaabbbbcc"
print(re.findall("a{1,2}",text)) # if we give re.findall("a{5,7}",text) then it will print empty list because there are only 5 a's together but if we give re.findall("a{2,4}",text) then it will print ['aaaa', 'a']
# Output: ['aaaa', 'a']
# Explanation: a{2,4} matches between 2 and 4 'a's together
# It matches 'aaaa' (4 a's) and 'a' (1 a, which is less than 2, so not matched)

## If we give n greater than m like {3,2} it will be invalid and will not match anything because n should be less than or equal to m

############ One Small Comparison Table ############
'''
| Quantifier | Meaning         | Example   |
| ---------- | --------------- | --------- |
| `+`        | 1 or more       | `\d+`     |
| `*`        | 0 or more       | `a*`      |
| `?`        | 0 or 1          | `u?`      |
| `{n}`      | exactly n       | `\d{10}`  |
| `{n,m}`    | between n and m | `\w{4,8}` |

'''

text = "Order IDs: 45 678 1234"
print(re.findall("\d+",text))

print(re.findall("\d{3}",text))

text = "color colour colouur"
print(re.findall("colou?r",text))
