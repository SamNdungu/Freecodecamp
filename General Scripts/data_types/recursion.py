import sys

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

i = 0

def greet():
    
    global i
    i += 1
    print("Hello ", i)
    greet()
    
greet()    

# A function to find factorial of a number using recursion

