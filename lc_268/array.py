# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n
# find the one that is missing from the array.

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

def missingNumber(self, nums: List[int]) -> int:
    arr = [-1] * (len(nums) + 1)
    for i in nums:
        arr[i] = i
    for n, j in enumerate(arr):
        if j == -1:
            return n
    return 0
        