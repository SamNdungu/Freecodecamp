pos = -1

def search(list, n):
    
    lower_bound = 0
    upper_bound = len(list) - 1
    
    while lower_bound <= upper_bound:
        
        mid_value = (lower_bound + upper_bound) // 2
        
        if list[mid_value] == n:
            globals()["pos"] = mid_value
            return True
        else:
            if list[mid_value] < n:
                lower_bound = mid_value + 1
            else:
                upper_bound = mid_value - 1 
                   
    return False

list = [2, 3, 4, 5, 6, 7, 9, 17, 19, 20, 209, 235, 902]   
n = int(input("Enter a number to search:\n"))

if search(list, n):
    print("Found at position ", pos + 1)
else:
    print("Not Found!")    
    