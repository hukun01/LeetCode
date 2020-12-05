# 95. Unique Binary Search Trees II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        Recursion.
        Note that 1..n is the in-order traversal for any BST with values 1 to
        n, so if we pick the i-th node as root, the left subtree will contain
        elements 1 to (i-1), and the right subtree will contain (i+1) to n. We
        use recursive calls to get back all possible trees for left and right
        subtrees and combine them in all possible ways with the root.

        Time: O(n G_n), where G_n is the Catalan number (4^n)/(n^(3/2))
        Space: O(n G_n)
        '''
        def build(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                lefts = build(start, i - 1)
                rights = build(i + 1, end)

                for left in lefts:
                    for right in rights:
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res

        if n == 0:
            return []
        return build(1, n)