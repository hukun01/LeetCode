# 1530. Number of Good Leaf Nodes Pairs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        '''
        DFS.
        In each recursion, compute the mappings between
        'distances from the node to its leaves' and 'the counts of distances'.
        Then combine the left mappings and the right one, for each
        (d1, c1) (d2, c2), d1+1+d2+1 is the shortest path between left leaves
        and right leaves. If d1+1+d2+1 is less than 'distance', then we get
        c1*c2 pairs of leaves.
        '''
        self.ans = 0
        def count(node):
            if not node:
                return {}
            if not node.left and not node.right:
                return {0: 1}
            left_leaf = count(node.left)
            right_leaf = count(node.right)
            leaf = Counter()
            for x, c in itertools.chain(left_leaf.items(), right_leaf.items()):
                if x + 1 < distance:
                    leaf[x + 1] += c
            
            for (l, c1), (r, c2) in itertools.product(left_leaf.items(), right_leaf.items()):
                if (l + 1) + (r + 1) <= distance:
                    self.ans += c1 * c2

            return leaf
        count(root)
        return self.ans