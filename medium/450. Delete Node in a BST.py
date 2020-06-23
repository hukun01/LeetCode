# 450. Delete Node in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''
        For the node to be deleted, use a combine method to merge its left and right
        children and return the merged child.
        Then we can recursively or iteratively find the node to be deleted, and call
        combine.
        '''
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
        """ 1/2 Recursive
        """
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
        """ 2/2 Iterative
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