# 61. Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        Find the size of the list, to handle cases in which k is greater than
        size. Then do k %= size, so we only rotate once.
        Then connect the tail to the old head,  and find the previous node of
        the new head in the list by advancing head node to (size - k - 1)
        steps. Disconnect the previous node of the new head and the new head,
        and return new head.

        Time: O(n) where n is the len(list)
        Space: O(1)
        '''
        node = head
        n = 0
        last = None
        while node:
            n += 1
            last = node
            node = node.next
        if n == 0 or (k := k % n) == 0:
            return head

        last.next = head
        prev = head
        for _ in range(n - (k % n) - 1):
            prev = prev.next
        new_head = prev.next
        prev.next = None
        return new_head