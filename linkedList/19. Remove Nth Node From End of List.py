# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Use 2 pointers, one goes first, another follows. The second pointer only starts after
        the first one has gone n steps. Note that second pointer needs to start from a dummy node
        in order to handle list with only one node, aka, when the result is None.
        '''
        first = head
        dummy = second = ListNode(0)
        dummy.next = head
        steps = 0
        while first:
            steps += 1
            first = first.next
            if steps > n:
                second = second.next
        second.next = second.next.next
        return dummy.next