# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        '''
        Maintaining current max and current min in a stack,
        through the tree from top to down.
        '''
        answer = 0
        stack = [(root, root.val, root.val)]
        while stack:
            node, curMax, curMin = stack.pop()
            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)
            answer = max(answer, curMax - curMin)
            if node.left:
                stack.append((node.left, curMax, curMin))
            if node.right:
                stack.append((node.right, curMax, curMin))
        return answer