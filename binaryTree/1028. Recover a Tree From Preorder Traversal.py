# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        num = ""
        depth = 0
        levelNodes = {}
		# we process the last node and the last depth when we encounter the '-', 
		# so add a '-' at the end to capture the final node
        S += "-"
        for c in S:
            if c.isdigit():
                num += c
            else:
				# continuous '-', keep adding depth
                if not num:
                    depth += 1
                    continue
                node = TreeNode(int(num))
                num = ""
				# root node
                if not levelNodes:
                    levelNodes[0] = [node]
                    depth += 1
                    continue
				# after adding root, we always have the parent node as the last node 
				# from the last level
                parent = levelNodes[depth - 1][-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                if depth not in levelNodes:
                    levelNodes[depth] = []
                levelNodes[depth].append(node)
                depth = 1
                    
        return levelNodes[0][0]