# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        We need a helper function to return the current max path that ends at the current node,
        and while we are exploring, we update the global maxPath by combining the 2 subtrees
        and the current value.
        It's important to return 0 if the current max path is less than 0, so we can do the 
        combining without worrying about the negative sums.
        '''
        answer = -float('inf')
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal answer
            answer = max(answer, left + right + node.val)
            return max(0, max(left, right) + node.val)
        dfs(root)
        return answer