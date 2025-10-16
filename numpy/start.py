import numpy as np

print(np.__version__)  # to check the verison

#array = np.array([1,2,3,4,5])
#array = array * 2
#print(array)

# MULTIDIMENSIONAL ARRAY

#array = np.array('a') # zero dimensional array
#print(array.ndim) #prints the

#array = np.array(['A','B','C','D'])  # one dimensional array
#print(array.ndim)

array = np.array([['A','B','C','D'],
                ['A','B','C','D'],  # 2 dimensional array
                ['A','B','C','D']])
#print(array.ndim)

# there should be a consistant number of lists within every list , if a list has 3 elements then every list should consist 3 elements


array1 = np.array([[['A','B','C','D'],['A','B','C','D'],['A','B','C','D']],
                [['A','B','C','D'],['A','B','C','D'],['A','B','C','D']],
                 [['A','B','C','D'],['A','B','C','D'],['A','B','C','D']]]) # 3d array

#print(array.ndim)

#array = np.array(['A','B','C','D'])
#print(array.shape)  # used to print the shape of the array

print(array1[2,0,0])   # multidimensional indexing 

# array[start:end:step]

# the start first index is for the rows and the second one id for the second ones


print(array[1:0:-1])  # row selections

print(array[1,2]) # column selections

# SCALAR ARITHMETIC (scalar means a singular value)

array2 = np.array([1,2,3])
print(array2 + 1)
print(array2 - 2)
print(array2*3)
print(array2 / 4)
print(array2 ** 5)

# VECTORIZED MATH FUNCTIONS (it is a single dimensional list)

print(np.sqrt(array2)) # used for the square root
print(np.round(array2)) # used for rounding the values
print(np.floor(array2)) # used for rounding down the number
print(np.ceil(array2))  # for round up
print(np.pi)


# EXERCISE

radii = np.array([1,2,3])
print(np.pi * radii ** 2)

# ELEMENT WISE ARITHMETIC

array3 = np.array([4,5,6])
print(array2 + array3)

scores = np.array([37,99,98,67,100,65,90])

print(scores >= 85 )

scores[scores < 70] = 0
print(scores)


# BROADCASTING

# Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger arrays shape 

# the dimensions have the ssame size
# OR
# One of the dimensions has a size of 1

#arr1 = np.array([[1,2,3,4]])
#arr2 = np.array([[1],[2],[3],[4]])

#print(arr1.shape)
#print(arr2.shape)

#print(arr1 * arr2)


# AGGREGATE FUNCTIONS = summarize data and typically return a single value
arr1 = np.array([[1,2,3,4] , [8,4,5,6]])
print(np.sum(arr1))
print(np.mean(arr1))
print(np.std(arr1))
print(np.average(arr1))
print(np.var(arr1))
print(np.min(arr1))
print(np.max(arr1))
print(np.argmin(arr1)) # it returns the index of the first minimum value
print(np.argmax(arr1))
print(np.sum(arr1) , axis = 0) # axis is 0 it means we are applying to all the columns
print(np.sum(arr1) , axis=1) # axis is 1 it means we are applying it to all the rows


# FILTERING = refers to the process of selecting elements from an array that match a given condition

ages = np.array([[21 , 22 , 34 , 23 , 19],
                 [39,22,15,99,18,19,20,21]])

teenagers  = ages[ages < 18]
adults = ages[(ages >= 25) & (ages < 65)]

print(teenagers)
print(adults)

adults1 = np.where(ages >= 18 , ages , -1)
print(adults1)   # where is used to preserve the original shape 

# where is lot slower than filtering because filtering uses boolean indexing 

# RANDOM NUMBERS

#rng = np.random.default_rng(seed=1)

#print(rng.integers(low= 1, high = 101 , size = (3,2)))  # the keywords low and high arent neccessary 
# we wanted 3 random numbers at a time so we set the size to 3
# we wanted a 2d array so we wrote 3,2
# we set seed because we wanted to reproduce the same results

# for floating point number

np.random.seed(seed=1)
print(np.random.uniform(low = -1  , high = 1 ,  size=(3,2)))

# shuffle an array

rng = np.random.default_rng()

arrayy = np.array([1,2,3,4,5,6])
rng.shuffle(arrayy)
print(arrayy)

fruits = np.array(['apple' , 'orange' , 'coconut' ,'pineapple' ])
fruit = rng.choice()
print(fruit)