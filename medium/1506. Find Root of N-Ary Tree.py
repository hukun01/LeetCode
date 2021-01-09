# 1506. Find Root of N-Ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        '''
        Transform + Single number.
        The O(n) space approach is trivial. To achieve constant space, the key
        observation is that we visit each node twice, one as itself, anoher as
        a child of other nodes, except for the root. In another word, all
        values appear twice except the root's value. Now this becomes the
        single number problem where xor all numbers would find the root value.

        Time: O(n) where n is the number of nodes
        Space: O(1)
        '''
        xor = 0
        for node in tree:
            xor ^= node.val
            for child in node.children:
                xor ^= child.val

        return next(node for node in tree if node.val == xor)