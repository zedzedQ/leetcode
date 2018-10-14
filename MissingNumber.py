# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# my solution 1
# sort the list
# traverse to check the difference between the current and previous entries
# edge cases: did not check the first and last value

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                return nums[i] - 1
        if len(nums) != nums[-1]:
            return len(nums)
        return 0

# my solution 2
# math, get the appropriate sum
# calculate the sum of all numbers in nums
# appropriate sum - actual sum

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for char in nums:
            sum += char
        a = len(nums)
        return ((1 + a) * a//2) - sum

# solution 3
# use XOR
# a perfect list is where the index and values would match

class Solution:
    def missingNumber(self, nums):
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ i ^ nums[i]
        return xor ^ i







