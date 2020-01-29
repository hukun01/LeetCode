# 250. Count Univalue Subtrees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """
        Do bottom-up / postorder traversal to determine if the 2 subtrees is uni-val,
        if yes, then check the current whole tree, and add 1 to the *global* count.
        """
        count = 0
        def isUnivalSubtree(node):
            if not node:
                return True
            left = isUnivalSubtree(node.left)
            right = isUnivalSubtree(node.right)
            if left and right:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
                nonlocal count
                count += 1
                return True
            return False
        
        isUnivalSubtree(root)
        return count