# <-----EXPLANATION---->
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given a sorted linked list, remove duplicates from the list and return the sorted, non-duplicate list

# <------CODE------>
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        current = head.next
        prev = head

        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next

        return head
