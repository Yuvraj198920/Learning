# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSum(nums: list[int], target: int) -> list[int]:
    for i, j in enumerate(nums):
        if abs(j) <= abs(target) and i < len(nums):
            for h, k in enumerate(nums[i+1 :len(nums)]):
                total = nums[i] + k
                if total == target:
                    return [i, h+i+1]

nums = [-1,-2,-3,-4,-5]
num = twoSum(nums, -8)
print (num)