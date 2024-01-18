pos = -1

def search(list, n):
    
    i = 0
    while i < len(list): 
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
        
    return False

list = [4, 20, 18, 9, 3, 5, 7, 6, 2]   
n = int(input("Enter a number to search:\n"))

if search(list, n):
    print("Found at position ", pos + 1)
else:
    print("Not Found!")    
    