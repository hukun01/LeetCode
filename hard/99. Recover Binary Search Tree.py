# 99. Recover Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        DFS inorder traversal.
        A BST with two elements swapped, when we inorder traverse this tree,
        the sequence should be ordered, except that one previous element is
        greater than at least one subsequent elements, and the last current
        element that is less than its previous element.
        These are the two that we want to swap back to correct the BST.
        """
        self.prev = None
        self.first = self.second = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
            
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val