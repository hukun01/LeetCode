# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        Iterate through the tree with inorder traversal.
        Leverage the generator and enumerate().
        
        Follow-up: use a LRU-like structure in which we also maintain a doubly-linked list,
        to get the O(k) time for kth smallest operation. While we also have the tree,
        and have O(h) insert and delete operation.
        '''
        def inorder(node):
            if not node:
                return None
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        for i, val in enumerate(inorder(root), start = 1):
            if i == k:
                return val