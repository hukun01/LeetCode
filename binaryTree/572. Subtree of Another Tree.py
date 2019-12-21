# 572. Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        '''
        Recursion
        '''
        def sameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and sameTree(s.left, t.left) and sameTree(s.right, t.right)
        return sameTree(s, t) or (s and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)))