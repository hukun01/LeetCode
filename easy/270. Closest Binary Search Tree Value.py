# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        The key here is to always compare the current answer to the current root.val.
        
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        """ 1/2 Recursive
        a = root.val
        kid = root.left if target < a else root.right
        if not kid:
            return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))
        """
        """ 2/2 Iterative
        """
        closest = root.val
        while root:
            closest = min((root.val, closest), key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest