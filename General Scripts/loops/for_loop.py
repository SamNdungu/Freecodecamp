for i in range(0, 201, 2):
    print(i)
    
for x in range(100, 201, -1):
    print(x)
    
for y in range(0, 201, 2):
    if y % 5 == 0:
        print(y)        
        
        
# continue keyword
for j in range(1, 101):
    
    if j % 3 == 0 and j % 5 == 0:
        continue
    
    print(j)
    
print("Bye")            
        
# pass keyword        
        
for k in range(0, 101):
    
    if k % 2 != 0:
        pass
    else:
        print(k)     
        
print("Bye")          