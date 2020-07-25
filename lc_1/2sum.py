# Two Sum
# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# # too slow
# def twoSum(nums, target):
# 	for i, n in enumerate(nums):
#         for j, m in enumerate(nums):
#             if j == i:
#                 continue
#             if n+m == target:
#                 return [i, j]
#     return []

def twoSum(nums, target):
	dict = {}
    for i, n in enumerate(nums):
        if target-n in dict:
            return [dict[target-n], i]
        dict[n] = i
    return []
