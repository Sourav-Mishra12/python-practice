
# solving some problem statements in python

# wap to add two numbers
a = 10
b = 20
sum = a+b 
print(sum)

# find the square root of a number

num = int(input("enter the number to check the square root : "))
print(num ** 2 )

# calculate the area of a circle given the radius 

radius = 6
pi = 3.14

print("the area of the circle is : ",pi * radius ** 2)

# convert celsius to farhenheit 

celsius = 32
farhenheit = (9/5 * celsius ) +32 
print("the farhenheit is : " , farhenheit)

# swap two nummbers withput using a third variable

num1 = 22
num2 = 25
print("value of num1 before : " , num1 , "value of num2 before : " , num2)

num1,num2 = num2,num1

print("value of num1 after : " , num1 , "value of num2 after : " , num2)

# check if a number is odd or not

number = int(input("enter the number to check if it is odd or not : "))

if number % 2 == 0 :
    print("the number is not odd it is even")
else :
    print(" it is an odd number")

# find the factorial of a number

def factorial(n):
    if n < 0 :
        raise ValueError ("Factorial cannot be defined for negative numbers ")
    
    result = 1
    for i in range (1 , n+1):
        result *= 1
    return result 
    
print(factorial(10))


# generate a multiplication table for a number

c = int(input("Enter the number to generate the multiplication table : ")).strip()

for i in range (1,11):
    print(c , "x" , i ,"=" , c*i)

# check if a number is prime or not

d = int(input("enter the number to check prime : "))

if d == 1 :
    print("1 is not considered enter any other number")
elif d % 1 == 0 and d % d == 0 :
     print("this number is prime number")
else :
     print("not a prime number ")


# find the sum of digits of a number

num3 = int(input("enter the number : "))
sum = 0

while True :
    sum += num3 % 10
    num3 = num3 // 10

print(sum)

# print all numbers from 1 to 100

for i in range(1,101):
    print(i)

# print the fibonacci sequence upto n terms

num4 = int(input("enter the number for fibonacci series : "))

a.b = 0,1 
for i in range(num4):
    print(a,end = " ")
    a,b = b , a+b

    