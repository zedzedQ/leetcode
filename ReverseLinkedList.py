# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# interstive solution
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while(head):
        	curr = head
        	head = head.nect
        	curr.next = prev
        	prev = curr
        return prev

# recursive solution
# n1 → … → nk-1 → nk → nk+1 → … → nm → None
# suppose we are now at nk, the head of new
# n1 → … → nk-1 → nk → nk+1 ← … ← nm
# thus we want nk+1.next eqaul to head
# and head.next = None


class Solution:
	def reverseList(self,head):
		if head == None or head.next == None:
			return head
		else:
			new = self.reverseList(head.next)
			head.next.next = head
			head.next = None
		return new