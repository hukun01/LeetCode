# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        The key here is to notice that if target < root.val,
        then the closest value must fall into the left part, otherwise
        will fall into the right part. Also, both parts need to include the root.
        
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        """ Recursive
        a = root.val
        kid = root.left if target < a else root.right
        if not kid:
            return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))
        """
        closest = root.val
        while root:
            closest = min((root.val, closest), key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest