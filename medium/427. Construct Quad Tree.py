"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        Recursion.
        Simply following the problem description leads to an suboptimal solution.
        We will repeatedly check the submatrices' values.
        To avoid that, we use a post-order style recursion to build the leaf nodes
        first, and from bottom up, we check those nodes values and merge them when
        they are all leaves and share the same value. If they don't satisfy this
        condition, they are just separate children for the current node.
        '''
        n = len(grid)
        def build(r0, c0, length):
            if length == 1:
                return Node(grid[r0][c0], True, None, None, None, None)

            subMatrixLength = length // 2
            topLeft = build(r0, c0, subMatrixLength)
            topRight = build(r0, c0 + subMatrixLength, subMatrixLength)
            bottomLeft = build(r0 + subMatrixLength, c0, subMatrixLength)
            bottomRight = build(r0 + subMatrixLength, c0 + subMatrixLength, subMatrixLength)

            allAreLeaves = topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
            sameValue = topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            if allAreLeaves and sameValue:
                return Node(grid[r0][c0], True, None, None, None, None)
            else:
                return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return build(0, 0, n)
