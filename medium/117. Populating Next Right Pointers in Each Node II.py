# 117. Populating Next Right Pointers in Each Node II
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        The key is to treat the next levels as linked lists.
        At each level, use a dummy node at the start, and cache the
        first child node in the next level.
        '''
        node = root
        while node:
            dummy = prev = Node()
            head = node
            while head:
                if head.left:
                    prev.next = head.left
                    prev = prev.next
                if head.right:
                    prev.next = head.right
                    prev = prev.next
                head = head.next
            node = dummy.next

        return root