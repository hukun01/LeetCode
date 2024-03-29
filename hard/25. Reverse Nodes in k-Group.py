# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
        Keep a counter, whenever we find k nodes, we start the reverse process.

        One *KEY* to keep the code concise is to do below reverse.
        Pass in the *exclusive* 'start' and 'end' of the interval to reverse
        the list between these 2 nodes exclusively, and return the reversed
        list's last node. The reason for doing this is to get access and be
        able to manage the two nodes outside the reversing sublist.

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
        dummy = pre = ListNode(next=head)
        
        def reverse(start, end):
            curr = start.next
            prev = end
            while curr != end:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            new_end = start.next
            start.next = prev

            return new_end

        count = 0
        while head:
            count += 1
            if count % k == 0:
                pre = reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next

        return dummy.next