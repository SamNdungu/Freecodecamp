def fact(n):
    
    f = 1
    
    for i in range(1, n + 1):
        f = f * i
        
    return f

x = int(input("Enter the number to find it's factorial: \n")) 
result = fact(x)

print(result)

# Using recursion
def fac(k):
    
    if k == 0:
        return 1
    
    return k * fac(k - 1)

result = int(input("Enter a number to find factorial: \n"))
print(fac(result))