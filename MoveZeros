# leetcode question 283
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# my solution
# traverse through the list 
# if met a 0, delete it
# concatenate one zero to the end

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for item in nums:
            if item == 0:
                nums.remove(item)
                nums.append(0)

# solution 2
# i is current index, j is the index of 0
# bubble sort through the list
# if the entry is 0, j will not increment
# thus when met with a non-zero entry, replace those two

class Solution:
	def moveZeros(self, nums):
		j = 0
		for i in range (len(nums)):
			if nums[i] != 0:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp
				j++


