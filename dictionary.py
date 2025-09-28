
# DICTIONARIES ALLOWS USER TO WRITE THE DATA IN THE FORM OF KEYS AND VALUES
# DICTIONARIES ARE ENCLOSED INSIDE CURLY BRACKETS {}
# KEYS AND VALUES ARE SEPERATED BY COLON { KEY : VALUE}
# EVERY KEY VALUE PAIR IS SEPERATED BY A , 

employee = {"name" : "sourav" , "age" : 21 , "gender" : "male"}
print(employee)
print(employee["age"])


# ----------------ITERATON IN DICTIONARY -----------------------

# printing all the keys

for key in employee:
    print(key)

# printing all the values one by one

for x in employee :
    print(employee[x])

# use value function

for x in employee.values():
    print(x)

# using item functions

for x,y in employee.items():
    print(x,"-" , y)


# -------------------- FUNCTIONS IN DICTIONARY ------------------

# get function (used to fetch value of any key)

x = employee.get("name")
print(x)

# items function (used to get the key values in form of tuple)

a = employee.items()
print(a)

# keys functions

b = employee.keys()
print(b)

# values functions

c = employee.values()
print(c)

# copy functions

d = employee.copy()
print(d)

# setdefault function

x = employee.setdefault("age", 22)
print(x)

# NESTED DICTIIONARIES

students = {1 : {"name" : "rishabh" , "age" : 23 , "gender" : "male"},
            2 : {"name" : "sakshi" , "age" : 22 , "gender" : "female"},
            3 : {"name" : "siddarth" , "age" : 24 , "gender" : "male"},
            4 : {"name" : "ritik", "age" : 23 , "gender" : "non-binary"}}

print("the age of " , students[2]["name"], "is" , students[2]["age"])

# PROBLEM SOLVING

# wap to sort the dict by values

dict1 = {"a" : 12 , "b" : 23 , "c" : 6 , "d" : 91 , "e" : 45}
dict1 = sorted(dict1.values())
print(dict1)

# wap to print a dict where the keys are the numbers between 1 and 15 and the values are squares of keys

dict2 = {}
for i in range(1,16):
    dict2[i] = i*i

print(dict2)

# wap to multiply all the items in a dict

dict3 = {"a" : 1 , "b" : 2 , "c" : 3 , "d" : 4 , "e" : 5}

mul = 1
for i in dict3:
    mul *= dict3[i]

print(mul)

# wap to sort a dict by keys

dict4 =  {"b" : 12 , "c" : 23 , "g" : 6 , "i" : 91 , "a" : 45}
dict4 = sorted(dict4.keys())
print(dict4)