"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """ The key is to use a dummy node at the start of each level,
        and have ANOTHER dummy node to cache the first child node in the next level.
        """
        cached = root
        while root:
            cur = temp = Node(0, None, None, None)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = temp.next
        return cached