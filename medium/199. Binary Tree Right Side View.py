# 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        Traverse the tree by level.
        '''
        ans = []
        queue = deque([root])
        while queue:
            last_val = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                last_val = node.val
                queue += [node.left, node.right]
            if last_val:
                ans.append(last_val)
        return ans