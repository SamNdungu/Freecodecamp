nums = [5 , 4, 2, 3, 6, 7, 9, 10]

it = iter(nums)
print(it) # Prints iterator object 
  
print(it.__next__()) # Prints values one by one...only the first one when called once
print(next(it)) # Prints values one by one...only the first one when called once


for i in nums: 
    print(i)

