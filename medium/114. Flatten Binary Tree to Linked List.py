# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        '''
        We need a global parameter to track the previous node so we can
        stitch it through the preorder traversal path.
        Also need to clear the left child in the previous node (it's already
        used, so safe to erase).
        '''
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode()
        def preorder(node):
            if not node:
                return
            rightCopy = node.right
            self.prev.left = None
            self.prev.right = node
            self.prev = node
            preorder(node.left)
            preorder(rightCopy)

        preorder(root)
