# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        
        Leverage the sorted feature of BST. 
        Just walk down from the root when both p and q are in the same subtree.
        """
        while root:
            if q.val < root.val > p.val:
                root = root.left
            elif q.val > root.val < p.val:
                root = root.right
            else:
                return root