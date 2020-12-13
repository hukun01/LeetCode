# 865. Smallest Subtree with all the Deepest Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        @lru_cache(None)
        def get_depth(node):
            if not node:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)
            return max(left, right) + 1

        def lca(node):
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            if left_depth == right_depth:
                return node
            if left_depth > right_depth:
                return lca(node.left)
            return lca(node.right)

        return lca(root)