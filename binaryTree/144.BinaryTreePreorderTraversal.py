# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ 1/2 Iterative with stack
        stack = [root]
        values = []
        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return values
        """
        """ 2/2 Morris traversal
        """
        values = []
        while root:
            if root.left:
                node = root.left
                while node.right != root and node.right:
                    node = node.right
                if node.right:
                    node.right = None
                    root = root.right
                else:
                    values.append(root.val)
                    node.right = root
                    root = root.left
            else:
                values.append(root.val)
                root = root.right
        return values