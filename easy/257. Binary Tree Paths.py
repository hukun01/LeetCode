# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        '''
        Note that the worst time and the best time is both O(n).
        '''
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        left = [str(root.val) + "->" + i for i in self.binaryTreePaths(root.left)]
        right = [str(root.val) + "->" + i for i in self.binaryTreePaths(root.right)]
        return left + right