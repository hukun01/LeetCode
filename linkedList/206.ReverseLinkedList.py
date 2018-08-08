# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        Use a dummy head to make code concise.
        
        :type head: ListNode
        :rtype: ListNode
        """
        prevHead = None
        while head:
            recordNext = head.next
            head.next = prevHead
            prevHead = head
            head = recordNext
        return prevHead