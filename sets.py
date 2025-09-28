
# SETS ARE UNORDERED COLLECTION OF DATA . EVERY ELEMENT INSIDE THE SET IS UNIQUE AND MUTABLE
# SETS ARE WRITTEN INSIDE THE CURLY BRACKETS
# THE VALUE INSIDE A SET IS SEPARATED BY ,
# MUTABLE MEANS ONCE CREATED , THEY CAN BE CHANGED 
# AN EMPTY SET IS DECLARED BY " SET() "

a = {"ironman" , "hulk" , "thor" , "captain america"}
b = {"superman" , "batman" , "wonder woman"}
c = { "hulk" , "thor"}

numbers = {3, 7, 2, 9, 12, 5, 7, 3, 15, 18, 21} # NO VALUE CAN BE REPEATED

print(numbers)
print(type(numbers))

for x in numbers :
    print(x)


# ------------------- SET FUNCTIONS ---------------------

# add 
numbers.add(100)
print("the number 100 is being added : ",numbers)

# pop (the will remove any value randomly from the set)
numbers.pop()
print("a number is being popped : ", numbers)

#remove (this will remove the value of our choice)
numbers.remove(100)
print("the number 100 is being removed : " , numbers)

# discard 
numbers.discard(3)
print("the number 3 will be removed : " ,  numbers)

# copy
numbers2 = numbers.copy()
print(numbers2)

# isdisjoint  (checks if two sets have no elements in common)
print(a.isdisjoint(b))

#issubset  (checks if all elements of one set are in another set)
print(a.issubset(b))
print(a.issubset(c))

#issuperset  ( checks if a set contains all elements of another set)
print(b.issuperset(a))
print(a.issuperset(c))

# update
a.update(c)
print(a)

# clear
a.clear()
print(a)

# union (it will return all the values of the respective sets)
print(a.union(b))
print(a.union(c))

# difference (it will return the values of SET A but not the common elements and also not the elements from SET B)
print(a.difference(c)) # [this method will provide us with a new set]

# difference update ()
a.difference_update(c)
print(a)   # this will update the exisiting set only

# intersection  (it will return the common values)
x = a.intersection(c)
print(x)

# intersection update 
a.intersection_update(c)
print(a)   # makes change in the original set

# symmetric difference (it wont provide the common values)
y = a.symmetric_difference(c)
print(y)

# symmetric difference update
a.symmetric_difference_update(c)
print(a)   # updating the exisiting sets


# ------------------- problem solving -------------------

# wap to find the max and min in a set

set1 = {12,22,33,44,678,889,0,999}
maximum = max(set1)
minimum = min(set1)
print("the min value is : ", minimum)
print("the max value is : ", maximum)

# wap to find common elements in three lists using sets

l1 = [1,5,6,8,2]
l2 = [4,5,6,7]
l3 = [1,9,6,2,5]

print(set(l1) & set(l2) & set(l3))

# wap to  find the difference between two sets

print(numbers.difference(set1))

# wap to remove an item from a set if it is present in the set

set2 = { 10,20,30,40,50 }
set2.discard(20)
print(set2)

# wap to check if a set is a subset of another set

print(set1.issubset(set2))
