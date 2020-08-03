# 872. Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        DFS with post-order traversal.
        Use yield and zip_longest to save space.
        """
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)
        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))