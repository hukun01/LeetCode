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