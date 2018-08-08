# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

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