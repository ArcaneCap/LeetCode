'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums: list[int], target: int) -> list[int]:

    seen = {}
    
    for i in range(len(nums)):
        # Calculate the difference needed for the target
        difference = target - nums[i]

        # If the difference is in the dictionary, we have a solution
        if difference in seen:
            # Return difference index and current number's index
            return [seen[difference], i]
       
        # Else, store the current number and its index in the dictionary
        seen[nums[i]] = i

      
# Expected out: [0,1]
print(twoSum(nums = [2,7,11,15], target = 9))

# Expected out: [1,2]
print(twoSum(nums = [3,2,4], target = 6))

# Expected out: [0,1]
print(twoSum(nums = [3,3], target = 6))