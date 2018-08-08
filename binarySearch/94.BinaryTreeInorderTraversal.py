# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def pushLeftChildren(stack, node):
            while node:
                stack.append(node)
                node = node.left
                
        stack = []
        values = []
        pushLeftChildren(stack, root)
        while stack:
            node = stack.pop()
            values.append(node.val)
            pushLeftChildren(stack, node.right)
                
        return values