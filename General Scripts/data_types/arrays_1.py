from array import *

arr = array("i", [])

n = int(input("Enter the length of an Array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
    
print(arr) 

# Getting index number manually
val = int(input("Enter the value to search: ")) 

k = 0 
for element in arr:
    if element == val:
        print(k)  
        break
    
    k += 1

# Using a function 
print(arr.index(val))
 