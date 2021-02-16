# 968. Binary Tree Cameras
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        '''
        1/2 Greedy + Post-order traversal.

        We have to cover leaf nodes, and there are 2 options for that:
        1. put a camera on the leaf node;
        2. put a camera on the leaf node's parent.
        Option 2 is always at least as good as option 1, so we should always
        do option 2.

        Starting from the bottom of the tree, if any of the node's children is
        not covered, we need a camera on the node. When adding a camera, we can
        cover the node's parent, itself, and its children.

        Note that we need to initialize the covered set with { None } because
        null child should be considered covered already.

        Also, to handle an edge case [0] where root is a leaf without parent,
        we need to check 'root not in covered' and add to answer if it's true.

        Time: O(n) where n is the number of nodes.
        Space: O(n)
        '''
        self.ans = 0
        covered = { None }
        def dfs(parent, node):
            if not node:
                return
            dfs(node, node.left)
            dfs(node, node.right)

            if node.left not in covered or node.right not in covered:
                self.ans += 1
                covered.update({ parent, node, node.left, node.right })

        dfs(None, root)
        return self.ans + int(root not in covered)

        '''
        2/2 Greedy + Post-order traversal, space optimized.

        Similar idea with 1/2, but here we leverage the return value from
        dfs(), and no need to track all covered nodes.

        Traverse the tree in post-order, there are 3 statuses to handle:
        1. return 0 if it's a leaf: it needs to be covered by the parent;
        2. return 1 if it's a parent of a leaf: it must have a camera;
        3. return 2 if it's covered without a camera, either because it's None,
           or because some of its direct children got a camera.

        Time: O(n)
        Space: O(h) where h is the tree height.
        '''
        self.ans = 0
        def dfs(node):
            if not node:
                return 2

            left = dfs(node.left)
            right = dfs(node.right)
            if 0 in {left, right}:
                self.ans += 1
                return 1

            return 2 if 1 in {left, right} else 0

        if dfs(root) == 0:
            self.ans += 1
        return self.ans