# 113. Path Sum II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        '''
        DFS
        Standard preorder traversal.
        '''
        self.ans = []
        def preorder(node, path = [], cur_sum = 0):
            if not node:
                return

            path.append(node.val)
            cur_sum += path[-1]

            if node.left == node.right == None:
                if cur_sum == targetSum:
                    self.ans.append(path[:])

            preorder(node.left, path, cur_sum)
            preorder(node.right, path, cur_sum)

            cur_sum -= path.pop()

        preorder(root)
        return self.ans