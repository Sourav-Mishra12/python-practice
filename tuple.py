
# TUPLES ARE THE COLLECTION OF ORDERED AND IMMUTABLE DATA
# FOR TUPLES NO BRACKETS ARE MANDATORY . BY CHOICE ONE CAN USE PARENTHESES
# THE VALUE INSIDE A TUPLE IS SEPARATED BY ,
# ONCE CREATED , TUPLES CANNOT BE CHANGED
# MULTIPLE DATATYPES CAN BE WRITTEN INSIDE A TUPLE

a = "apple" , "mango" , "banana" , "kiwi"
print(type(a))

# if i have only one value in my tuple 

b = ("sourav mishra")
print(type(b))  # this will be of string type

c = ("sourav mishra" , )
print(type(b))  # this will be of tuple class


# ----------- SLICING AND ITERATION --------------

phones = ("vivo" , "iphone" , "lava" , "nokia")
print(phones[1:3])

print(phones[:3])
print(phones[2:])

print(phones[::2])  # skipping two values (1 only you know exclusive index behaviour)
print(phones[::-1])   # reverse

# iteration with for loop

for i in phones :
    print(i)

# along with range and length in for loop

for i in range (len(phones)):
    print(phones[i])

# using while loop

i = 0
while i < (len(phones)):
    print(phones[i])
    i+=1

# conversion of tuple and tuple functions

# REMEMBER :- IN ORDER TO MUTATE A TUPLE WE SHOULD CONVERT IT INTO A LIST 

phones = list(phones)  # we have converted the tuple in a list
phones.append("redmi")
print(phones)
phones = tuple(phones)  # we have converted the list back to tuple
print(type(phones))
print(phones)

print("the occurence of redmi is : ",phones.count("redmi"))
print("the index of redmi is : ",phones.index("redmi"))


# given a tuple for which write a function to find the name of the student with the highest score

students = (('sourav' , 80) , ('srishti' , 90 ) , ('sakshi' , 99))

def top_student(data):

    # using max function to calculate the max value
    return max(data , key = lambda y : y[1])[0]

print("the top student is : " , top_student(students))

# wap to count the occurences in a tuple

def count_values(tup , value):
    return tup.count(value)

tup1 = (1,2,22,2,2,3,4,55,6,7,5,55,22)
print("the occurence of 22 is : ",count_values(tup1,22))

# wap to find the first occurence of index of an element

def find_index(tup,value):
    if value in tup:
        return tup.index(value)
    else:
        return -1
    
tup2 = (1,2,3,4,4,4,5,5,6,7,8,5,2,4)
print(find_index(tup2,2))
print(find_index(tup2,9))


# swap two tuples without using a temp variable

a = (1,23,3,44)
b = (1,22,33,44)

a,b = b,a
print("a : ", a)
print("b :", b)


# TUPLES ARE FASTER THAN LISTS IN CASE OF ITERATION BECAUSE THEY ARE IMMUTABLE
# BECAUSE TUPLES ARE IMMUTABLE AND HASHABLE , THEY CAN BE USED AS KEYS IN DICTIONARIES
# TUPLES USE LESS MEMORY SPACE THAN LISTS
