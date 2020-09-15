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
        Check the node:
        if it has right,
            if the right has left, then the leftmost is the successor,
            if the right has no left, the right is the successor.
        if it has no right, then check its parent,
            if it's the parent's left child, then parent is the successor,
            if it's the parent's right child, then go further to the parent's parent.
        '''
        if not node:
            return None
        if node.right:
            r = node.right
            while r.left:
                r = r.left
            return r
        p = node.parent
        while p and p.left != node:
            node, p = p, p.parent
        return p