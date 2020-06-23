# 222. Count Complete Tree Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        '''
        Binary search.
        Based on the property of complete tree, if the right subtree's
        height (determined by its left chain) is one less than the total
        height h, left subtree is full at the h-th level, and we can add
        the count of left subtree, and continue the process on the right
        subtree.
        Otherwise, the right subtree is full at the (h-1)-th level, we can
        add the count of right subtree, and continue the process on the
        left subtree.
        Note that we let the root level to have 0 height.
        '''
        def get_height(node):
            if not node:
                return -1
            return 1 + get_height(node.left)

        nodes = 0
        h = get_height(root)
        while root:
            if get_height(root.right) == h - 1:
                nodes += 1 << h
                root = root.right
            else:
                nodes += 1 << (h - 1)
                root = root.left
            h -= 1
        return nodes