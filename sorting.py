def sorting(nums):
    for i in range(len(nums -1)):
        minpos= i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j

   
   
    temp =nums[i]
    nums[i]=nums[minpos]
    nums[minpos]=temp


    

nums = [7,6,8,4,1,2]
sorting(nums)
print(nums)