from numpy import *

arr = array([
    [12, 3, 45, 23, 20, 21],
    [8, 9, 12, 2, 4, 17]
])

print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

# Create 1D array from multi-dimensional 
arr1 = arr.flatten()
print(arr1)

# Create multi-dimensional array from 1D array
arr2 = arr1.reshape(3, 4)
print(arr2)

arr3 = arr1.reshape(2, 2, 3)
print(arr3)

 
# Creating a matrix
myArray = array([
    [1, 2, 3],
    [4, 5, 6]
])

m = matrix(myArray)
print(m)

# Above code can be written as below
m1 = matrix('1 2 3; 6 4 5; 6 7 8')
m2 = matrix('2 4 7; 9 10 23; 3 15 11')

print(m1)
print(m2)


# Diogonal elements
print(m1.diagonal)
print(m1.min)
print(m1.max)

# Adding matrices
m4 = m1 + m2
print(m4)

# Multiplying matrices
m3 = m1 * m2
print(m3)
