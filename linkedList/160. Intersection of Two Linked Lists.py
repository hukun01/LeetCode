# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        Form a virtual cycle from each list, by connecting the tail of list A
        to the head of list B. Assuming list A's part1 has x length, list B's part1
        has y length, and the shared part has z length.
        Then node a would traverse (x + y + z) length, and same for node b, so they will
        meet at the intersection.
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a