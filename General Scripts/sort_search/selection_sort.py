def sort(nums):
    
    for i in range(8):
        min_position = i
        for j in range(i, 9):
            if nums[j] < nums[min_position]:
                min_position = j
                
        temp = nums[i]
        nums[i] = nums[min_position]
        nums[min_position] = temp
        
        print(nums)       
        
nums = [4, 20, 18, 9, 3, 7, 5, 6, 2] 
sort(nums)
print(nums)                 
                
                
                