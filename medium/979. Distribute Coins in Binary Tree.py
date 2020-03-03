# 979. Distribute Coins in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        '''
        Post-order traverse.
        In each dfs sub-procedure, return the number of coins that should be
        passed up to the parent. Negative number means that the child needs
        coin from parents.
        The total number of coins that need to be passed through each node is
        the number of moves.
        Similar to 517. Super Washing Machines
        '''
        ans = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal ans
            ans += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return ans