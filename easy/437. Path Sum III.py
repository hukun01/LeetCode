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
        Prefix sums in tree.
        Use prefixSum at each node, so we can get the sum of any downwards
        paths in constant time.
        Also need to decrement the prefixSum count when exiting the recursion,
        because we are switching to another branch.

        Time: O(n) where n is the number of nodes in tree.
        Space: O(n)

        Similar to 560. Subarray Sum Equals K.
        '''
        count = Counter({0: 1})
        
        def dfs(node, prefix_sum):
            if not node:
                return 0

            prefix_sum += node.val
            ans = count[prefix_sum - sum]

            # Only increment the count after we check it, and before we
            # enter subtrees.
            count[prefix_sum] += 1

            ans += dfs(node.left, prefix_sum)
            ans += dfs(node.right, prefix_sum)
            count[prefix_sum] -= 1
            return ans

        return dfs(root, 0)