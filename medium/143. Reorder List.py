# 143. Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        Slow & fast pointers + reverse list + interleaving lists.
        '''
        prev = ListNode(next=head)
        slow = fast = prev
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        prev = None
        while mid:
            mid.next, mid, prev = prev, mid.next, mid
        head2 = prev
        while head and head2:
            next1 = head.next
            next2 = head2.next
            head.next = head2
            head2.next = next1
            head = next1
            head2 = next2