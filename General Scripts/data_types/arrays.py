from array import *

values = array("i",[2, 3, 4, 5, -6, -8])
print(values.buffer_info())
print(values.reverse())

for value in values(6):
    print(value)
    
    
newArr = array(values.typecode, (a * a for a in values))    
    
for val in newArr(6):
    print(val)    
  
  
# Using while loop  
j = 0

while j < len(newArr):
    print(newArr[j])  
    j += 1
    