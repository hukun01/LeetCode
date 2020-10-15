# 148. Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        Bottom up merge sort with O(1) space.
        Find the total length of the list.
        Iterate steps from 1 until it exceeds the total length, doubling it
        each time. Merge 1 node with 1 node, then 2 nodes with 2 nodes, etc,
        until step > length, which means we have merged 'step0' nodes, and
        step0 >= length // 2.
        '''
        if not head or not head.next:
            return head
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < size:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                tail = self.merge(left, right, tail)
            step <<= 1
        return dummy.next

    def split(self, head, n):
        '''
        Split the list (starting from head) into two lists,
        the first list contains n nodes.
        Return the second list's head.
        '''
        for _ in range(1, n):
            if head:
                head = head.next
        if not head:
            return None
        second = head.next
        head.next = None
        return second
    
    def merge(self, l1, l2, head):
        '''
        Merge two sorted lists, and append the merged list to head.
        Return the tail of the merged list.
        '''
        cur = head
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        while cur.next:
            cur = cur.next
        return cur