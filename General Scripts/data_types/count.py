def count(lst):
    
    even = 0
    odd = 0
    
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
            
    return even, odd   

lst = [21, 20, 19, 810, 28, 23, 17, 18, 90, 1019, 100, 106, 202, 20, 1, 109, 971]       

even, odd = count(lst)  
print(even)
print(odd)

print("Even Numbers are: {} and Odd Numbers Are: {}".format(even, odd))