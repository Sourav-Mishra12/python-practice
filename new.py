
#FIND THE SUM OF FIRST 10 ODD NUMBERS

sum = 0
n = 0
while n <= 20:
    if n % 2 != 0 :
        sum+= n 
    n += 1
print("the sum of all the first ten odd nums are" , n)


# WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 12 UPTO 100 NUMBERS

for i in range (1,101):
    if i % 8 == 0 and i % 12 == 0 :
        print(i)


# WRITE A PROGRAM TO CREATE A BILLING SYSTEM

while True:
    name = input("ENTER CUSTOMER NAME : ")
    total = 0

    while True:
        print("enter the amount and quantity ")
        amount = float(input("enter the amount : "))
        quantity = float(input("enter the quantity : "))
        total += amount * quantity 
        repeat = input("do you want to add more items? (yess/no) : ")
        if repeat.lower() == "no":
            break 
    print("-"*20)
    print("NAME : " , name)
    print("AMOUNT TO BE PAID : " , total)
    print("-"*20)
    print("THANK YOUUUU")

    repeat_1 = input("do you want to get to the next customer ? (yess/no) : ")
    if repeat_1.lower() == "no":
        break


# WAP TO FIND THE LENGTH OF A STRING 

sentence = input("enter the string : ")
print("the length of the sentence is :  ",len(sentence))

# WAP TO CHECK HOW MANY TIMES ALPHABET O IS REPEATING

a = input("enter the string : ").lower()
print("the occurences of the alphabet o is : ",a.count("o"))

# WAP TO CONVERT A SENTENCE INTO LOWER AND UPPER CASE

b = input("enter the string : ")
print("the string in lower case : ",b.lower())
print("the string into upper case : ",b.upper())

# WAP TO CONVERT THE STRING INTO TITLE

c = input("enter the string : ")
print("the string will be converted into title : ",c.title())

# PATTERN PROBLEM 

for i in range(1,6):   #rows
    for j in range(1,i+1):    #columns
        print(j , end = " ")
    print()


for i in range(1,6):   #rows
    for j in range(1,i+1):    #columns
        print("*" , end = " ")
    print()


# PATTERN PROBLEM

for i in range(1,6):   
    for j in range(1,i+1):   
        print( i , end = " ")
    print()


# PATTERN PROBLEM 

for i in range(1,6):   #rows
    for j in range(6 , i , -1):    #columns
        print( i , end = " ")
    print()

# PATTERN PROBLEM 

for i in range(1,6):
    for j in range (5,i,-1):
        print(" " , end = " ")
    for k in range(i):
        print("*" , end = " ")
    print()

# PATTERN PROBLEM

for i in range (1,6):
    for j in range(i,0,-1):
        print(j , end =  " ")
    print()

# PATTERN PROBLEM

for i in range (1,6):
    for j in range(1,i+1):
        print("*", end = " ")
    print()
for i in range(5,0,-1):
    for k in range(0,i-1):
        print("*" , end = " ")
    print()
