
# FUNCTIONS ARE A SET OF CODE , WHICH ONCE CREATED , THEY CAN BE USED THROUGHOUT THE PROGRAM 

# FUNCTIONS HELP BREAK OUR PROGRAM INTO SMALLER PARTS AND HELPS IT LOOK MORE ORGANIZED AND MANAGEABLE

# DEFINE THE FUNCTION (BODY) , CALL THE FUNCTION (NAME)

def hello():           # DEFINING THE FUNCTION
    # function body
    print("hello world")

hello()  # calling the function 

def add (x,y):   # function with parameters
    print(x+y)

add(10,88)   # using arguments

# WE USE PARAMETRES WHILE WRITING THE FUNCTION 
# WE USE ARGUMENTS WHILE CALIING THE FUNCTION

def rect(length,width):
    print("the area of the rectangle is : " , length*width)

rect(10,10)

# arbitary positinal arguments

# (an arbitrary argument allows you to pass a variable number of arguments to a function. This is useful when you don't know ahead of time how many arguments might be passed to the function.)

def hello(*name):
    print("hello my name is " , name[1])

hello("sourav" , "srishti" , "sakshi")


def my_func(*args):
    for arg in args :
        print(arg)

my_func(1,2,3,4,5,6)

# arbitary keyword arguments 

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="sourav", age=21)

# exqmple using both of it

def describe_pet(pet_name, *traits, **details):
    print(f"My pet's name is {pet_name}.")
    for trait in traits:
        print(f"- Trait: {trait}")
    for key, value in details.items():
        print(f"- {key}: {value}")

describe_pet("Buddy", "friendly", "furry", species="dog", age=3)


# RETURN STATEMENTS AND RECURSION 

# (return keyword in python is used to exit a function and return the value of the function)

def addition(a,b):
    return (a+b)

print(addition(10,20))

# RECURSION 

# ( recursion is most commonly used mathematical and programming concept)
# ( recursion means a function can call itself , giving us a benefit of looping through data in order to get a result)

def factorial(num):
   
    if num == 1:
        return 1 
    else :
        return num * factorial(num-1)
    
    
try :
    number = int(input("ENTER A NUMBER TO CHECK FACTORIAL : "))
    
    if number < 0 :
        print("FACTORIAL IS NOT FOR NEGATIVE NUMBERS ")
    else:
        result = factorial(number)
        print(f"the factorial of {number} is {result}")

except ValueError :
    print("PLEASE ENTER A VALID INPUT")

# ADVANATAGES OF RECURSION

# THEY MAKE THE CODE LOOK CLEAN AND ORGANISED
# BY THE USE OF RECURSIVE FUNCTIONS A COMPLEX TASK CAN BE BROKEN DOWN INTO SMALLER SUB PARTS
# SEQUENCE GENERATION BECOMES EASIER

# DISADVANTAGES OF RECURSION

# RECURSIVE FUNCTIONS TAKE UP A LOT OF MEMORY
# SOMETIMES THE LOGIC BECOMES HARD TO FOLLOW
# DEBUGGIN IS VERY COMPLICATED AND HARD

# LAMBDA FUNCTION 

# it is used when an anonymous function is required for a short period
# it can take numerous arguments
# it can only have one expression

a = lambda b : b*5
print(a(10))

x = lambda a,b,c : (a+b) * c
print(x(3,7,10))

# LOCAL AND GLOBAL VARIABLES 

# local variables are restricted to only one block of code and cannot be changed throughout the program

x = 24
print("first variable x " , x)
def xyz():
    x = 23
    return(x)

print(xyz())
print(x)

# global variables are not restricted to one block of code and they can be changed throughout the program

y = 900
print("the first value of y : " , y)
def vvv():
    global y 
    y = 800
    return y

print(vvv())
print(y)

# PROBLEM SOLVING 

# waf to find the max of 3 numbers
def max_find(num1,num2,num3):

    return max(num1,num2,num3)


num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))

print("the max number is : " , max_find(num1,num2,num3))

# waf to create and print a list where the values are square of numbers between 1 to 30

def create_list():
    l = []
    for i in range (1,31):
        l.append(i**2)
    
    return l 

print(create_list())

# waf that takes a number as a parameter and check if the number is prime or not

def check_prime(num):

    if num == 1 :
        print("it is not a prime number")

    if num == 2 :
        print("it is a prime number")
    
    if num > 2:
       for i in range(2,num):
           if num % i == 0:
              print("not a prime number")
              break
       else :
           print("it is a prime number")

check_prime(37)

# waf to summ all the numbers in a list

def add_all(numbers):       # solution 1
    total = 0

    for i in numbers :
        total += i
    return (total)

print("the sum of all the items : ",add_all([1,2,3,4,5,6,7,8]))


def add(numbers):     # solution 2 using recursion

      if len(numbers) == 1:
          print(numbers[0])

      else:
         return((numbers[0]) + add(numbers[1:]))

print(add([1,2,3,4,5,6,7,8]))         

# waf to solve the fibonacci series using recursion

def fibonacci(num):
    if num == 1 :
        return (0) 
    elif num == 2 :
        return (1)
    else:
        return(fibonacci(num1) + fibonacci(num-2))
    
print(fibonacci(7))

