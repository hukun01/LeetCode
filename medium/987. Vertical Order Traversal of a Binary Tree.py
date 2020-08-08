# 987. Vertical Order Traversal of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        '''
        DFS / BFS.
        The key is to store both column and row info and sort the values
        at the same positions.
        Similar to 314. Binary Tree Vertical Order Traversal.
        '''
        cols = defaultdict(list) # (row, val)
        def dfs(node, col, row):
            if not node:
                return
            cols[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)
            
        dfs(root, 0, 0)
        ans = [[] for _ in range(len(cols))] 
        i = 0
        for col in range(min(cols), max(cols) + 1):
            ans[i] = [val for row, val in sorted(cols[col])]
            i += 1

        return ans