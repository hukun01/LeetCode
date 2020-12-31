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

        Iterate by step, from *1* until it exceeds the total length, doubling
        the step each time.
        Initially we merge 1 node with 1 node, then 2 nodes with 2 nodes, etc,
        until step > length.

        The split() split the current list into two lists, the first list
        contains n nodes. And it returns the second list's head. (We already
        have the first list's head)

        The merge() merges two sorted lists, and append the merged list to
        the given tail. And it returns the tail of the merged list, so we can
        append the next round of merge sort result to this tail.

        Time: O(n log(n)) where n is len(list)
        Space: O(1)
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
            sorting_head = dummy.next
            tail = dummy
            while sorting_head:
                list1 = sorting_head
                list2 = self.split(list1, step)
                sorting_head = self.split(list2, step)
                tail = self.merge(list1, list2, tail)
            step <<= 1
        return dummy.next

    def split(self, head, n):
        for _ in range(1, n):
            if head:
                head = head.next
        if not head:
            return None
        second = head.next
        head.next = None
        return second
    
    def merge(self, l1, l2, tail):
        cur = tail
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