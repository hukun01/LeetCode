# 382. Linked List Random Node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Reservoir sampling.
    Keep replacing the answers with a decreasing probability. For all elements,
    the accumulated probabilities are the same.
    Note that the first element will be selected at first, so we always have
    something to return.

    Time: O(n) for each get(), where n is size of the linked list.
    Space: O(1)
    '''
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        node = self.head
        count = 0
        ans = 0
        while node:
            count += 1
            if random.randrange(count) == 0:
                ans = node.val
            node = node.next
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()