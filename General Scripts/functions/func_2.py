# A function with 2 arguments
def person(name, age=18): # Default age = 18
    print(name)
    print(age + 5)
    
person(age=28, name="Samuel")  
person("Samuel")  # Takes 18 as default age and adds 5 


def sum(*b): #  *b means we can have multiple arguments
    c = 0
    
    for i in b:
        c = c + i
    
    print(c) 
    
sum(5, 4, 29, 20, 12, 1, 7)    
    