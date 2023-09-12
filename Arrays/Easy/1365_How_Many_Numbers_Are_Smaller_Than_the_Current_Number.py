'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    
   
    temp = sorted(nums)
    order = {}

    for i in range(len(nums)):
        if temp[i] not in order:
            order[temp[i]] = i

    for i in range(len(nums)):
        nums[i] = order[nums[i]]
    
    return nums


# E. out : [0, 0, 0, 0]
print(smallerNumbersThanCurrent(nums = [7,7,7,7]))
