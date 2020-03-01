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
        """ 1/2 Iterative using stack: 
        To make the logic clear, use a nested function pushLeftNodes()
        to push all the left children of one Node and itself into the stack.
        We push all the left children of root and root into the stack until there's no more nodes.
        Then we pop from the stack which we'd call cur. Add cur to result list.
        Iteratively call pushAllLeft() on cur's right child.

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
        """ 2/2 Morris traversal: See 0.Notes.txt
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