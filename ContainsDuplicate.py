# 217

# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

# if it is an empty array, return False

# my solution
class Solution(object):
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums = sorted(nums);
    for i in range(1, len(nums)):
    	if nums[i-1] == nums[i]:
    		return True
    return False


# solution 1
# use set in python
class Solution(object):
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))