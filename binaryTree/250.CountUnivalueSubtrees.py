# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        Do bottom-up / postorder traversal to determine if the 2 subtrees is uni-val,
        if yes, then check the current whole tree, and add 1 to the *global* count.
        
        :type root: TreeNode
        :rtype: int
        """
        def isUnivalSubtree(node, count):
            if not node:
                return True
            left = isUnivalSubtree(node.left, count)
            right = isUnivalSubtree(node.right, count)
            if left and right:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
                count[0] += 1
                return True
            return False
        count = [0]
        isUnivalSubtree(root, count)
        return count[0]