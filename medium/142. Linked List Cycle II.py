# 142. Linked List Cycle II
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
        pre = ListNode(0)
        pre.next = head
        fast = slow = pre
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        new = pre
        while slow != new:
            slow = slow.next
            new = new.next

        return slow