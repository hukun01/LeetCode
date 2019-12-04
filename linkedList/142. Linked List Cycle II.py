# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        To determine whether there is a cycle, do below:
        Use a start node as a dummy previous node that connects to head.
        Start the slow and fast both from start. Inside the loop, break when they intersect.
        If we exhaust the fast node and didn't break, there is no cycle.
        
        If there is a cycle, use a slow2 from start, and progress slow and slow2 together until they intersect
        at the cycle entry.
        '''
        if not head or not head.next:
            return None
        start = ListNode(0)
        start.next = head
        slow = fast = start
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        slow2 = start
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow