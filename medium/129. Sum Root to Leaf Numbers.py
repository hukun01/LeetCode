# 129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        '''
        1/2 Recursion by tracking the root to leaf path
        '''
        self.ans = 0
        def dfs(node, path):
            if not node:
                return
            path.append(node.val)
            if node.left == node.right == None:
                add = sum(a * 10 ** (len(path) - 1 - i) for i, a in enumerate(path))
                self.ans += add
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return self.ans
        '''
        2/2 Recursion by tracking the running sums
        '''
        def sum_tree(node, curr_sum):
            if not node:
                return 0
            if node.left == node.right == None:
                return curr_sum * 10 + node.val
            new_sum = curr_sum * 10 + node.val
            return sum(sum_tree(child, new_sum) for child in [node.left, node.right])
        return sum_tree(root, 0)