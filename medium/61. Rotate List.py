# 61. Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        Find the size of the list, to handle cases in which k is greater than size.
        Then do k %= size, so we only rotate once.
        Then connect the tail to the old head,  and find the previous node of the new
        head in the list by advancing head node to (size - k - 1) steps.
        Disconnect the previous node of the new head and the new head, and return new head.
        '''
        n = head
        sz = 0
        last = None
        while n:
            sz += 1
            last = n
            n = n.next
        if sz == 0 or (k := k % sz) == 0:
            return head

        last.next = head
        prev = head
        for _ in range(sz - (k % sz) - 1):
            prev = prev.next
        newHead = prev.next
        prev.next = None
        return newHead