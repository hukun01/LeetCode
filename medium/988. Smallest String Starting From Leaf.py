# 988. Smallest String Starting From Leaf
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        '''
        DFS
        Find all the root to leaf paths and compare them.

        Note that we can't stop early with something like:
        min(dfs(left) + root.val, dfs(right) + root.val),
        because the list comparison thinks the shorter list is smaller
        if two lists share the prefix.
        An example is [0, 1, 3] and [0, 1, 0, 3] (both from leaf to root),
        the above logic would return the first path, which is wrong.
        If we try to override the default list comparison by considering
        the list length, then an example like [0, 1, 3] and [0, 1, 4, 3]
        would still fail.
        Overall, we need to get the full path and compare them.
        '''
        self.ans = [27]
        def preorder(node, path):
            if not node:
                return
            path.append(node.val)
            if node.left == node.right == None:
                self.ans = min(self.ans, path[::-1])
            preorder(node.left, path)
            preorder(node.right, path)
            path.pop()
        preorder(root, [])
        return ''.join(chr(ord('a') + c) for c in self.ans)