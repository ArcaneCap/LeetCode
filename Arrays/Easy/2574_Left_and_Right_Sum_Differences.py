'''
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

    answer.length == nums.length.
    answer[i] = |leftSum[i] - rightSum[i]|.

Where:

    leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
    rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return the array answer.
'''

''' Big O of n^2'''
# def leftRightDifference(nums: list[int]) -> list[int]:
#     return [(abs(sum(nums[:i]) - sum(nums[i+1:]))) for i in range(len(nums))]


def leftRightDifference(nums: list[int]) -> list[int]:
    
    if len(nums) == 0:
        return [0]


    ans = []
    sum_left, sum_right = 0, sum(nums)

    for i in nums:
        sum_right -= i
        ans.append(abs(sum_right-sum_left))
        sum_left += i

    return ans
        

# E. out: [15, 1, 11, 22]
print(leftRightDifference(nums = [10,4,8,3]))