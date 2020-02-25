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
        Use prefixSum at each node, so we can get the sum of any downwards
        paths in constant time.
        Also remember to decrement the prefixSum count when exiting the recursion,
        because we are switching to another branch.

        Similar to 560. Subarray Sum Equals K.
        '''
        count = collections.Counter({0: 1})
        
        def dfs(node, preSum):
            if not node:
                return 0
            
            preSum += node.val
            ans = count[preSum - sum]

            # only increment the count after we check it, and before we enter subtrees.
            count[preSum] += 1
            
            ans += dfs(node.left, preSum)
            ans += dfs(node.right, preSum)
            count[preSum] -= 1
            return ans
        
        return dfs(root, 0)