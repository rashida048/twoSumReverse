def twoNums(nums, target):
    result = []
    i = 0
    while i < (len(nums)-1):
        j = i + 1
        while j < (len(nums)):
            if (nums[i] + nums[j]) == target:
                result.append(i)
                result.append(j)
            j += 1
        i += 1 
    return result 

print(twoNums([3,2,4], 6))
        

    
