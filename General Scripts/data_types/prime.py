num = int(input("Enter a Number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not a Prime Number!")
        break
    
else:
    print("It's a prime number")    
    
# Best method to find prime numbers
starting_range = int(input("Enter the lowest value: "))
ending_range = int(input("Enter the highest value: "))

print("The prime numbers in this range are: ")

for num in range(starting_range, ending_range + 1):
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                break
            
        else:
            print(num)      