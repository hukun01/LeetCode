# 510. Inorder Successor in BST II
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        '''
        If a node has right child, then successor is the right child's leftmost child;
        Otherwise, 
            if a node is its parent's left child, then successor is the parent;
            if a node's parent is its grandparent's left child, then successor is the parent
        '''
        if not node:
            return None
        if node.right:
            r = node.right
            while r.left:
                r = r.left
            return r
        while node.parent:
            if node == node.parent.left:
                return node.parent
            node = node.parent
        return None