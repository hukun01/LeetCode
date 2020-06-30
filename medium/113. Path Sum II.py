# 113. Path Sum II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        '''
        DFS
        Standard preorder traversal.
        '''
        self.ans = []
        def preorder(node, path = [], curr_sum = 0):
            if not node:
                return
            path.append(node.val)
            curr_sum += path[-1]
            if node.left == node.right == None:
                if curr_sum == sum:
                    self.ans.append(path[:])
            preorder(node.left, path, curr_sum)
            preorder(node.right, path, curr_sum)
            curr_sum -= path.pop()
        preorder(root)
        return self.ans