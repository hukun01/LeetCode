# 156. Binary Tree Upside Down
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        '''
        1/2 Reverse the root-left branch with a stack.

        Key is to understand the special shape of the tree.
        Then to flip it, just reverse from root to all its left node,
        and link the right nodes based on the example.
        O(n) space where n is the number of tree nodes
        '''
        if not root:
            return None
        lefts = []
        while root:
            lefts.append(root)
            root = root.left
        new_root = node = lefts.pop()
        while lefts:
            new_child = lefts.pop()
            node.left = new_child.right
            node.right = new_child
            new_child.left = new_child.right = None
            node = new_child
        return new_root
        '''
        2/2 Reverse the root-left branch in place.
        This is like reversing a linked list.
        O(1) space.
        '''
        cur = root
        last_right = prev = None
        while cur:
            nex = cur.left
            
            cur.left = last_right
            last_right = cur.right
            cur.right = prev
            
            prev = cur
            cur = nex
        return prev