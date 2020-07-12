# 662. Maximum Width of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        '''
        This is a binary tree, so each time the level increments, the number
        of nodes doubles.
        Find the position for each node, and at each level, the max width
        would be the right position - left position + 1.
        '''
        if not root:
            return 0
        q = deque([(root, 1)])
        width = 0
        while q:
            width = max(width, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, pos << 1))
                if node.right:
                    q.append((node.right, (pos << 1) + 1))
        return width