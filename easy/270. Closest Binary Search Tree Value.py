# 270. Closest Binary Search Tree Value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        '''
        The key here is to always compare the current answer to the current
        root.val.
        1/2 Recursive
        '''
        a = root.val
        kid = root.left if target < a else root.right
        if not kid:
            return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))
        '''
        2/2 Iterative
        '''
        closest = root.val
        while root:
            closest = min((root.val, closest), key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest