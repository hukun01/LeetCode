# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        Use a helper function to return the max sum from a single path that starts
        from the current node.
        While traversing the tree, we update the global answer by combining the 2
        single paths and the current value. We use max(0, left) and max(0, right)
        to exclude the single paths if their sums are negative.
        '''
        answer = -inf
        def singlePathSum(node):
            if not node:
                return 0
            left = singlePathSum(node.left)
            right = singlePathSum(node.right)
            nonlocal answer
            answer = max(answer, max(0, left) + max(0, right) + node.val)
            return max(left, right, 0) + node.val
            
        singlePathSum(root)
        return answer
