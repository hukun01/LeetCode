# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Use a dummy head to make code concise.
        """
        prev = None
        while head:
            cachedNext = head.next
            head.next = prev
            prev = head
            head = cachedNext
        return prev