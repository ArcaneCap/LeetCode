'''
Given a 0-indexed integer array nums of length n and an integer target, 
return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target. 
'''

def countPairs(nums: list[int], target: int) -> int:
    
    counter = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] + nums[i] < target:
                counter+=1
    
    return counter

# Exp. out: 3
print(countPairs(nums = [-1,1,2,3,1], target = 2))

# Exp. out : 10
print(countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))