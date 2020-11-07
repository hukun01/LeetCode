# 445. Add Two Numbers II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        Reverse the output.
        To not reverse input, an easy way is to stack all nodes and pop them,
        but this requires space O(N) where N is the total number of nodes.
        Although the output needs O(N) as well, we can make the intermediate
        process with constant space, by reversing the output list.
        Step1: Add all nodes together, without handling carry-overs, as
        carries can propagate backwards, so we need to reverse the output list.
        Step2: Reverse the output list, go through it and handle carries.
        Step3: Reverse back the output list, this is the answer.
        Time: O(N).
        Space: O(1).
        '''
        def get_len(l):
            ans = 0
            while l:
                l = l.next
                ans += 1
            return ans
        n1, n2 = get_len(l1), get_len(l2)
        prev = dummy = ListNode(0)
        if n1 < n2:
            n1, n2 = n2, n1
            l1, l2 = l2, l1
        while n1 > n2:
            prev.next = ListNode(l1.val)
            l1 = l1.next
            prev = prev.next
            n1 -= 1
        for _ in range(n1):
            prev.next = ListNode(l1.val + l2.val)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next

        def reverse(l):
            pre = None
            while l:
                nxt = l.next
                l.next = pre
                pre = l
                l = nxt
            return pre
        ans = cur = reverse(dummy.next)
        carry = 0
        prev = None
        while cur:
            val = carry + cur.val
            cur.val = val % 10
            carry = val // 10
            prev = cur
            cur = cur.next
        if carry:
            prev.next = ListNode(carry)
        return reverse(ans)