#### ***** Patterns ***** ####

# Pattern 1
'''
*
*
*
*
*
'''
print("##### Pattern1 ######")
for i in range(5):
    print("*")

'''
🧠 Thinking

Rows = 5

Each row has only 1 star

No change per row

🧠 Rule

👉 If output per row is fixed → no inner loop needed
'''

# Pattern 2
'''
*****
*****
*****
*****
*****
'''
print("##### Pattern2  #####")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

'''
🧠 Thinking

Rows = 5

Each row prints 5 stars

🧠 Rule

👉 Rectangle = rows loop + fixed stars loop
'''

# Pattern 3

'''
*
**
***
****
*****
'''
print("##### Pattern 3 #####")
for i in range(5):
    for j in range(i+1):
        print("*",end="") # If we not pass end="" it will print in new line for each iteration
    print() 

# Pattern 4
'''
1
12
123
1234
'''
print("##### Pattern 4 #####")
for i in range(4):
    for j in range(i+1):
        print(j+1,end="")
    print()


# Here in outer loop we have range(4) means it have 0,1,2,3 four values
# after for inner loop we have for j in range(i+1) means in 
# outer loop we have first value 0
# then it will comes to inner loop with '0' value then i+1 --> 0+1 ==> 1 ==> that means it is not equals to '1' value it is just range i.e. range(1) means we have only '0' then
# it goes to inner loop print statement i.e. 'j+1' means in inner loop we have range value '0' those '0' goes to print statement and in print we have 'j+1' then it is '0+1' then it is 1
# and it will checks for any another print statement there we have empty print() means it is new line here our 1st iteration is completed and went to 2nd iteration 
# here outer loop we have '1' then in inner loop we have i+1 means 1+1 ==> 2 i.e. range(2) means we have two values 0,1
# then first '0' goes to print statement there '0+1' means '0',next we have another value '1'it will also goes to print '1+1' means it is '2' and it will end the loop and it will follows same for every iteration

# Pattern 5:
'''
*****
****
***
**
*
'''
print("##### ** Pattern5 ** #####")
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()


# Pattern 6
'''
12345
1234
123
12
1
'''
print("##### ** Pattern6 ** #####")
for i in range(5):
    for j in range(1, 6 - i):
        print(j, end="")
    print()

# Pattern 7
'''
1
22
333
4444
'''
print("##### ** Pattern7 ** #####")
for i in range(4):
    for j in range(i+1):
        print(i+1,end="")
    print()

# Pattern 8
'''
    *
   **
  ***
 ****
*****
'''
print("##### ** Pattern8 ** #####")
for i in range(5):
    print(" " * (4-i) + "*" *(i+1))

# Pattern 9
print("##### ** Pattern9 ** #####")
for i in range(5):
    for j in range(5,i,-1):
        print(j, end="")
    print()

# Pattern 10
print("##### ** Pattern10 ** #####")
for i in range(4):
    for j in range(2*i+1):
        print("*",end="")
    print() 

# Pattern 11
print("##### ** Pattern11 ** #####")
for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print("*",end="")
    print()