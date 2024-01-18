nums = [12, 16, 18, 21, 26, 31]

for num in nums:
    
    if num % 5 == 0:
        print(num)
        break # Ensures the loops runs once and only first number divisible by 5 is returned. Otherwise, Not Found is printed.

else:
    print("Not Found!")    