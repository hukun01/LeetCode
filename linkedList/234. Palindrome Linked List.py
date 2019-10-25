# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        Reverse the first half of the list, compare it with the second half;
        Ignore the middle one if the number of nodes is odd.
        '''
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev, slow.next, slow = slow, prev, slow.next
            
        if fast:
            slow = slow.next
        while prev and prev.val == slow.val:
            prev = prev.next
            slow = slow.next
        return not prev