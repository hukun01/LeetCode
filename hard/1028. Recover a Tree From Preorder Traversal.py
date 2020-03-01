# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        levels = {}
        num = ""
        depth = 0
        S += "-"
        for c in S:
            # continuous '-', keep adding depth
            if c != '-':
                num += c
            else:
                if not num:
                    depth += 1
                    continue
                node = TreeNode(int(num))
                num = ""
                if depth not in levels:
                    levels[depth] = []
                levels[depth].append(node)
                if depth > 0:
                    parent = levels[depth - 1][-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                depth = 1
        return levels[0][0]