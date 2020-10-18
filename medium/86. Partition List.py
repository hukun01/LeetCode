# 86. Partition List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
        Split the list into 2 sub lists, one with smaller values, another
        with big or equal values. And join them at the end.
        Use dummy nodes to handle potentially empty lists.
        '''
        small = n1 = ListNode(0)
        big = n2 = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = n2.next
        return n1.next