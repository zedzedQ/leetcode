# Given an array of size n, find the majority element. 
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


# my solution
# use a dictonary
# traverse through the list
# key: char, value: freq
# traverse through the dictionary
# output the key whose value is greater than n/2

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        for item in freq:
            if freq[item] > len(nums) // 2:
                return item

# solution 2
# sort the list
# the middle value must be the marjority element

class Solution:
	def majorityElement(self, nums):
		nums = sorted(nums)
		return nums[len(nums)/2]

# solution 3
# Moore Voting Algorithm
# traverse through the list
# set the majorEl to be the potential majority Elem
# cancel out the count of majorEl for all the different values
# only works if majorEl exists

class Solution:
	def majorityElement(self, nums):
		majorEl = nums[0]
		count=0
		for char in nums:
			if char == majorEl:
				count += 1
			else:
				count -= 1
			if count == 0:
				majorEl = char
				count = 1

		return majorEl

