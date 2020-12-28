# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        Reverse the first half of the list, compare it with the second half;
        Ignore the middle one if the number of nodes is odd.
        In this implementation we let the second half to be always >= first
        half in length, so if the total length is odd, we will ignore the last
        one in the reversed list (which is originally the middle node).

        Time: O(n) where n is len(list)
        Space: O(1)
        '''
        slow = ListNode(next=head)
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        def reverse(node):
            pre = None
            while node:
                nex = node.next
                node.next = pre
                pre = node
                node = nex
            return pre
        second_head = slow.next
        slow.next = None
        second_head = reverse(second_head)
        while second_head and head and second_head.val == head.val:
            second_head = second_head.next
            head = head.next
        if second_head is None:
            return head == second_head == None
        return head == second_head.next == None