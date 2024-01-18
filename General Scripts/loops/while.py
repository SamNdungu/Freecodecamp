i = 1

while i <= 5:
    print("Samuel ", end="")
    
    j = 1
    while j <= 4:
        print("Loves you ", end="")
        j += 1
        
    i += 1
    print()    
    

# Break keywords    
av = 5

x = int(input("How many candies do you want?"))
              
i = 1
while i <= x:
    
    if i > av:
        print("Candy out of stock")
        break
    
    print("Candy")
    i += 1
    
print("Thanks for shopping with us!")    
