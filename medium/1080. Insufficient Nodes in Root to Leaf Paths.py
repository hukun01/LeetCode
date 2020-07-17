# 1080. Insufficient Nodes in Root to Leaf Paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        '''
        This is a recursive function that returns the node, if the node is sufficient, 
        otherwise returns None.
        
        If the root is leaf, we compare the limit and root.val, and return root
        if it's sufficient, otherwise return None.

        If root is not leaf, we call the same function on children nodes with updated
        limit = limit - root.val.

        At the end, if a non-leaf node does not have children, meaning its children
        are all insufficient, so this non-leaf node needs to be None as well, so return None.
        '''
        if not root:
            return None
        if not root.left and not root.right:
            return root if root.val >= limit else None
        
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None