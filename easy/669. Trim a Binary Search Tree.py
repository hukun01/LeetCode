# 669. Trim a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        '''
        1/2 Recursive.
        This is essentially a preorder traversal. Leverage BST's property.
        If node.val <= low, discard all its left, check its right.
        If node.val > high, discard all its right.

        Time: O(n) where n is the tree size.
        Space: O(h) where h is the height of the tree
        '''
        def preorder(node):
            if not node:
                return None
            if low <= node.val <= high:
                node.left = preorder(node.left)
                node.right = preorder(node.right)
                return node
            elif node.val < low:
                return preorder(node.right)
            else: # node.val > high:
                return preorder(node.left)

        return preorder(root)
        '''
        2/2 Iterative.
        The idea is the same as the recursive solution.

        A few keys to make it work:
        1. Need to track the parent node, and isLeft flag, so we can assign
           potentially new child nodes. The new child node can also be None.
        2. When current node is out of range, we need to explore its left or
           right, and inherit the isLeft flag from previous level, so we can
           stitch the new node to its grandparent later.

        Time: O(n) where n is the tree size.
        Space: O(h) where h is the height of the tree
        '''
        stack = [(root, None, False)]
        ans = None
        while stack:
            #print(f"stack {[(n.val if n else 'None', p.val if p else 'None', flag) for n, p, flag in stack]}")
            node, parent, isLeft = stack.pop()
            if parent:
                if isLeft:
                    parent.left = node
                else:
                    parent.right = node
            if not node:
                continue
            if low <= node.val <= high:
                ans = ans or node # take the first good node as the new root
                stack.append((node.right, node, False))
                stack.append((node.left, node, True))
            elif node.val < low:
                stack.append((node.right, parent, isLeft))
            else:
                stack.append((node.left, parent, isLeft))
        return ans