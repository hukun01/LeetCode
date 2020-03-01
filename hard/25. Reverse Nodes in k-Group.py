# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
         Keep a counter, whenever we find k nodes, we start the reverse process.
        To reverse, we pass in the prev and tail to reverse the list between
        these 2 nodes exclusively, and return the reversed list's last node.

        After each reverse, we need to update the prev and head for the next reverse.

        There is a difference between these two statements!!
        The FIRST one is wrong because 'curr' got modified after the first assignment,
        so 'curr.next' would be updated before it gets assigned!!
        curr, curr.next, prev = curr.next, prev, curr
        curr.next, curr, prev = prev, curr.next, curr

        Better to use below:
            cachedNext = curr.next
            curr.next = prev
            prev = curr
            curr = cachedNext
        '''
        def reverse(start, end):
            prev = end
            curr = start.next
            while curr != end:
                curr.next, curr, prev = prev, curr.next, curr
            last = start.next
            start.next = prev
            return last
        dummy = prev = ListNode(0)
        dummy.next = head
        count = 0
        while head:
            count += 1
            if count % k == 0:
                prev = reverse(prev, head.next)
                head = prev.next
            else:
                head = head.next
        return dummy.next