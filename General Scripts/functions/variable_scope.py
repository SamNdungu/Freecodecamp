a = 10 # Global variable

def something():
    
    # We can access the global variable, a = 10 here inside the function if we did'nt specify local variable, a = 15
    
    # a = 15 #  a = 10, a = 15, Local variable,  ##########Uncomment this to use a as a global variable###########
    
    # We can ignore local variable, a = 15 and use global variable, a = 10 using global keyword
    
    #########comment these two lines to use a as a local variable##########  
    global a
    a = 15 # Both a's = 15
    
    print("A, inside the function", a)
     
something()

print("A, outside the function", a)
    
    
# Second example
b = 10
print(id(b))

def thing():
    b = 9
     
    x = globals()["b"]
    print(id(x))
    print("B, inside the function", b)
    
    globals()["b"] = 20

thing()  

print("B, outside the function", b)  
    
    