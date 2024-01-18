a = 5
b = 0

try:
    print("Resource open")
    print(a / b)
    num = int(input("Enter a Number:"))
    print(num)
    
    
except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by zero:", e)

except ValueError as e:
    print("Invalid Input, Please enter an integer!")  
    
except Exception as e:
    print("Something went wrong...")      
    
finally:
    print("Resource closed")
      
print("Bye")
