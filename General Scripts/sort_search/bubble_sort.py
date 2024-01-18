def sort(nums):
    
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                
nums = [4, 20, 18, 9, 3, 5, 7, 6, 2] 
sort(nums)
print(nums)                 
                
                
                