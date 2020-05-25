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
        '''
        def dfs(node, bit):
            if not node:
                return 0
            bit ^= 1 << (node.val - 1)
            ans = dfs(node.left, bit) + dfs(node.right, bit)
            if node.left == node.right == None:
                if bit & (bit - 1) == 0: # check if bit is a power of 2.
                    ans += 1
            return ans

        return dfs(root, 0)
        '''
        2/2 DFS with counter of the values.
        '''
        self.ans = 0
        def isPalin(count):
            odds = [v for v in count.values() if v % 2 != 0]
            return len(odds) == 0 or (len(odds) == 1 and odds[0] % 2 == 1)
            
        def dfs(node, count):
            if not node:
                return
            count[node.val] += 1
            if node.left == node.right == None:
                if isPalin(count):
                    self.ans += 1
            else:
                dfs(node.left, count)
                dfs(node.right, count)
            count[node.val] -= 1
    
        dfs(root, Counter())
        return self.ans