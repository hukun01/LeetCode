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
        """ Morris traversal
        """
        values = []
        cur = root
        while cur:
            if cur.left:
                node = cur.left
                while node.right != cur and node.right:
                    node = node.right
                if not node.right:
                    node.right = cur
                    cur = cur.left
                else:
                    node.right = None
                    values.append(cur.val)
                    cur = cur.right
            else:
                values.append(cur.val)
                cur = cur.right
        return values
        """ Iterative using stack
        if not root:
            return []
        stack = []
        values = []
        def pushLeftNodes(node, stack):
            while node:
                stack.append(node)
                node = node.left
        pushLeftNodes(root, stack)
        while stack:
            node = stack.pop()
            values.append(node.val)
            pushLeftNodes(node.right, stack)
        return values
        """