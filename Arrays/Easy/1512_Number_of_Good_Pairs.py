'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''


def numIdenticalPairs(nums: list[int]) -> int:
    
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    ans = 0
    for frequency in freq.values():
        ans += (frequency**2 - frequency)//2
    
    return ans


# Expected out: 4
print(numIdenticalPairs(nums = [1,2,3,1,1,3]))

# Expected out: 6
print(numIdenticalPairs(nums = [1,1,1,1]))

# Expected out: 0
print(numIdenticalPairs(nums = [1,2,3]))