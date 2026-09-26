# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        1/2 Heap sort.

        Note: according to Python3 doc, tuple in heapq may collide.
        Tuple comparison breaks for (priority, task) pairs if the priorities
        are equal and the tasks (ListNode) do not have a default comparison order.
        So we use (priority, listIndex, listHead) as the tuple.

        Time: O(n log(k)) where n is the total number of nodes
        Space: O(k)
        '''
        heap = []
        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))
        dummy = prev = ListNode(0)
        while heap:
            val, idx, node = heappop(heap)
            prev.next = node
            prev = node
            if node.next:
                heappush(heap, (node.next.val, idx, node.next))
        return dummy.next
        '''
        2/2 Merge sort. Divide and Conquer.

        Do't merge list1 and list2, then list3, this time complexity will be bad.
        Instead, merge every two lists from the end of the list to the start of the
        list, and keep shrinking the range until we reduce the range to [0].

        Time: O(n log(k))
        Space: O(1)
        '''
        if not lists:
            return None

        def mergeTwoLists(a, b):
            dummy = pre = ListNode(0)
            while a and b:
                if a.val < b.val:
                    pre.next = a
                    a = a.next
                else:
                    pre.next = b
                    b = b.next
                pre = pre.next
            pre.next = a or b
            return dummy.next

        k = len(lists)
        while k > 1:
            for i in range(k // 2):
                lists[i] = mergeTwoLists(lists[i], lists[k - 1 - i])
            k = (k + 1) // 2
        return lists[0]
