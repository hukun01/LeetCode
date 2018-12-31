# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """ 1/2: Intuitive recursive approach with getDepth, but not efficient!

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
        """
        """
        2/2: DFS recursive approach with getDepth, return -1 to indicate the tree is not balanced.
        The getDepth() here actually bears two messages, one is the actual depth if return non-negative value,
        another is to indicate that the tree is not balanced by returning -1.
        """
        def getDepth(root):
            if not root:
                return 0
            left = getDepth(root.left)
            if left == -1:
                return -1
            right = getDepth(root.right)
            if right == -1:
                return -1
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1
        return getDepth(root) != -1