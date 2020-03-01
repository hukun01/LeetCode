# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def combine(left, right):
            if not left:
                return right
            if not right:
                return left
            node = right
            while node.left:
                node = node.left
            node.left = left
            return right 
        """ 1/3 Recursive
        def delete(root, key):
            if not root:
                return None
            if root.val == key:
                return combine(root.left, root.right)
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root
        return delete(root, key)
        """
        """ 2/3 Iterative
        """
        node = root
        parent = None
        while node and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right
        if not node:
            return root
        replacement = combine(node.left, node.right)
        if not parent:
            return replacement
        if node == parent.left:
            parent.left = replacement
        if node == parent.right:
            parent.right = replacement
        return root
        """ 3/3 Recursive
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        return root
        """