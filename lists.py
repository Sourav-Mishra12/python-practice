# LISTS ARE THE COLLECTION OF ORDERED AND MUTABLE DATA
# LISTS ARE WRITTEN INSIDE THE SQUARED BRACKETS
# THE VALUE INSIDE A LIST IS SEPARATED BY ,
# MUTABLE MEANS ONCE CREATED , THEY CAN BE CHANGED
# MULTIPLE DATAYPES CAN BE WRITTEN INSIDE A LIST

fruits=["mango","apple","banana"]
print(fruits)

random = ["sourav", 90 , 90.88 , False]
print(random[3])  # IT WILL PRINT THE VALUE ON THE THIRD INDEX (90.88)
print(random[0])  # IT WILL PRINT THE VALUE AT THE ZERO INDEX (sourav)
print(random[-2]) # IT WILL PRINT THE SECONF LAST VALUE {negative indexing}

print(random[0:3]) # SLICING 
print(random[:2])
print(random[::2]) 

print(random[::-1]) # it will revrese the list


# -------------------- LIST ITERATION -----------------------

# iteration using for loop

a = ["sourav","somo","bunty","siddharth"]
for i in a :
    print(i)

# iteration using for loop with range and length function

for i in range (len(a)):
    print(a[i])

# iteration using while loop 

i = 0
while i < (len(a)):
    print(a[i])
    i += 1

# using short-hand for loop

[print(i) for i in a ]


#  --------------------- LIST FUNCTIONS -------------------------

print(len(a))   # to find the length of the list

print(a.count("sourav"))   # to find the occurences of the element

a.append("honey singh")
print(a)   # used to add element at the last index

a.insert(2,"bhaijaan")
print(a)   # using this method we can add any element at any particular index

a.remove("sourav")
print(a)   # remove the element

print(a.pop(1))   # to remove any value for the index

b = a.copy()
print(b)   # to copy the elements from any other list

print(a.index("bhaijaan"))  # to find any value and know its index

c = ["srk","samantha"]
a.extend(c)
print(a)   # to extend any particular list

print(a.reverse())  # reverse krna hai bhai

print(a.sort())  # function ke naam mei hi kaam hai asc order mei


# ---------------------- LIST COMPREHENSION ----------------------

l1 = ["sourav" , "srishti" , 90 , 99 , 100.99 , 99.78]
l3 = [i for i in l1]
print(l3)     # used to copy the elements from l1 to l3
              # we can also use conditional statements


# ----------------------- PROBLEM SOLVING ---------------------

list1 = ["power" , "pochita" , "katanaman" , "denji" , "makima"]

# wap to swap first and fourth element

list1[0],list1[3] = list1[3],list1[0]
print(list1)

# wap to add a new value at the second position

list1.insert(1 , "Danger")
print(list1)

# wap to delete a value from 3rd position

list1.pop(2)
print(list1)


list2 = [1,2,3,4,5,6,7]

# wap to multiply all the numbes in the list

mul = 1
for i in list2 :
    mul *= 1
print(mul)

# wap to get the largest number from the list

list2.sort()   # first arrange the list in asc order
print("the largest value of the list is : ",list2[-1])  # the last index is the biggest element


