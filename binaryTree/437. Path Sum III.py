# 437. Path Sum III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        '''
        Similar to 560. Subarray Sum Equals K.
        Use prefixSum at each node, so we can get the sum of any downwards
        paths in constant time. Also remember to decrement the prefixSum count
        when exiting the recursion.
        '''
        count = collections.Counter()
        count[0] += 1
        
        def dfs(node, preSum):
            if not node:
                return 0
            
            preSum += node.val
            ans = count[preSum - sum]
            count[preSum] += 1
            
            ans += dfs(node.left, preSum)
            ans += dfs(node.right, preSum)
            count[preSum] -= 1
            return ans
        
        return dfs(root, 0)