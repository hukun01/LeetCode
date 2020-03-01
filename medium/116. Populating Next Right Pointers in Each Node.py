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
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # The key here is to leverage the next pointer, 
        # and process one level per inner loop.
        while root and root.left:
            recordNext = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                root = root.next
            root = recordNext