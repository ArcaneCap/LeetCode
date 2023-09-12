'''
Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

def runningSum(nums: list[int]) -> list[int]:
    
    running_sum = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        nums[i] = running_sum
    
    return nums

# E. out: [1,3,6,10]
print(runningSum(nums = [1,2,3,4]))

# E. out: [1,2,3,4,5]
print(runningSum(nums = [1,1,1,1,1]))

# E. out: [3,4,6,16,17]
print(runningSum(nums = [3,1,2,10,1]))