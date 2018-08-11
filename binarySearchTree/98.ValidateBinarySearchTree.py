# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        The key is to keep track of the previous node.
        
        :type root: TreeNode
        :rtype: bool
        """
        """ 1/2 Recursive: inorder, keep track of the previous node.
        prev = None
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev and node.val <= prev.val:
                return False
            prev = node
            return inorder(node.right)
        
        return inorder(root)
        """
        """ 2/2 Iterative: also inorder.
        """
        def pushNodeAndLeft(node, stack):
            while node:
                stack.append(node)
                node = node.left
        stack = []
        prev = None
        while root or stack:
            pushNodeAndLeft(root, stack)
            root = stack.pop()
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = root.right
        return True