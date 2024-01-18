# Method 1
# Program to display fibonacci sequence upto n_th term
n_terms = int(input("How many terms:\n")) # Enter 20 for exampla

# First 2 terms
n1, n2 = 0, 1
count = 0

# Check if n < 0
if n_terms < 0:
    print("Enter a positive integer")

# If there's one term, return n1
elif n_terms == 1:
    print("Fibonacci sequence upto: ", n_terms)    
    print(n1)

# Generate fibonacci sequence
else:
    print("Fibonacci sequence")
    while count < n_terms:
        print(n1)
        nth = n1 + n2 
        
        # Update values
        n1 = n2
        n2 = nth
        count += 1   

# Method 2
# Function for nth fibonacci number
def fiboacci(n):
    
    a = 0
    b = 1
    
    # Check if n < 0
    if n < 0:
        print("Incorrect Input, Please enter a value greator than or equal to zero")
        
    elif n == 0:
        return 0
    
    elif n == 1:
        return b    
    
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b     
    
print(fiboacci(50))    
    