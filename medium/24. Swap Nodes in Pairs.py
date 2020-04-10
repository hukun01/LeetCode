# 24. Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        Use below notation for clear view of the lists swap. And use x,y = y,x to swap.
        pre->(a->b)->c  =>  pre->(b->a)->(c->null)
        
        BE CAREFUL when updating the next pointers on nodes, below example can be surprising.
        a, a.next = b.next, x  # on the left, 'a.next' may hit null ref because b.next is None.
        '''
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next