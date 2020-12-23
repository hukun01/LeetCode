# 110. Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        1/2: Intuitive recursive approach with getDepth, but not efficient!

        Time: O(n^2) where n is the number of nodes
        Space: O(h) where h is the height of the tree
        '''
        def getDepth(root):
            if not root:
                return 0
            return max(getDepth(root.left), getDepth(root.right)) + 1
        if not root:
            return True
        left = getDepth(root.left)
        right = getDepth(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        2/2: DFS recursive approach with getDepth, return -1 to indicate the
        tree is not balanced.
        The getDepth() here actually bears two messages, one is the actual
        depth if return non-negative value, another is to indicate that the
        tree is not balanced by returning -1.

        Time: O(n)
        Space: O(h)
        '''
        def getDepth(node):
            if not node:
                return 0
            left = getDepth(node.left)
            right = getDepth(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return getDepth(root) != -1