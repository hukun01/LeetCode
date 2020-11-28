# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        Note that: according to Python3 doc, tuple in heapq may collide: 
        Tuple comparison breaks for (priority, task) pairs if the priorities are 
        equal and the tasks do not have a default comparison order.

        Also note that this tuple is not only the 2-element tuple, it's anything in parenthesis.
        Hence, make a triplet (node.val, index, node), such that there is no two (node.val, index)
        combination that can collide within the heapq.
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