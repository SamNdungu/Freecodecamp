from numpy import *

arr = array([1, 2, 3, 4, 5], int)

# Add 5 to each element in the array
arr1 = arr + 5
print(arr1)

arr2 = array([2, 5, 6, 7, 8], int)
arr3 = array([9, 4, 12, 4, 6], int)

# Add two arrays - ve ctorized operations
arr4 = arr2 + arr3
print(arr4)

# Copy array - You don't get two arrays in the memory though. We see this by printing their address in memory 

# Method 1
arr2 = arr3 # Aliasing 
print(arr2)
print(arr3)

# Method 2 - Shallow copy
arr2 = arr3.view() # Shallow copy
arr2[1] = 7 # Changing an element in one array changes the same element in the other array
print(arr2)
print(arr3)

# Method 3 - Deep copy
arr2 = arr3.copy() # Deep copy
arr2[1] = 8 # Changing an element in one array does not change the same element in the other array
print(arr2)
print(arr3)




# Checking their address in memory
print(id(arr2))
print(id(arr3))

# Other functions
print(sin(arr4))
print(log(arr4))
print(sqrt(arr4))
print(sum(arr4))
print(min(arr4))
print(max(arr4))
print(concatenate([arr2, arr3]))



