# 1457. Pseudo-Palindromic Paths in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        '''
        1/2 DFS with bit set.
        We can use an integer as a bit set to record the values we have seen,
        because the value range is small as [1, 9].
        With XOR operation, we only keep the values that occur in odd times.

        Time: O(n) where n is len(tree)
        Space: O(n)
        '''
        def dfs(node, bit):
            if not node:
                return 0
            bit ^= 1 << (node.val - 1)
            ans = dfs(node.left, bit) + dfs(node.right, bit)
            if node.left == node.right == None:
                if bit & (bit - 1) == 0: # reset the lowest bit
                    ans += 1
            return ans

        return dfs(root, 0)
        '''
        2/2 DFS with counter of the values. This uses more space in practice
        but can handle any potential values other than digits.

        Time: O(n) where n is len(tree)
        Space: O(n)
        '''
        def preorder(node, val2freq):
            if not node:
                return 0

            ans = 0
            val2freq[node.val] += 1
            if not node.left and not node.right:
                ans += int(sum(v % 2 == 1 for v in val2freq.values()) <= 1)

            ans += preorder(node.left, val2freq)
            ans += preorder(node.right, val2freq)
            val2freq[node.val] -= 1
            return ans

        return preorder(root, Counter())