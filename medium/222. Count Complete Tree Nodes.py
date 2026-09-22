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
        the full count of left subtree nodes, and continue the process on
        the right subtree.
        Otherwise, the right subtree is full but one less than the left subtree,
        we can add the count of right subtree (2**right_subtree_h), and
        continue the process on the left subtree.
        
        Each subtree includes the current root.
        '''
        def get_height(node):
            if not node:
                return 0
            return 1 + get_height(node.left)

        nodes = 0
        h = get_height(root)
        while root:
            # left subtree's height is one less than the total height
            # this is by definition of a complete tree
            left_subtree_h = h - 1
            right_subtree_h = get_height(root.right)
            if right_subtree_h == left_subtree_h:
                # left subtree is full, count all the nodes including current root
                nodes += 1 << left_subtree_h
                root = root.right
            else:
                # right subtree is also full but one level less than the left subtree
                assert right_subtree_h == left_subtree_h - 1
                nodes += 1 << right_subtree_h
                root = root.left
            h -= 1
        return nodes
