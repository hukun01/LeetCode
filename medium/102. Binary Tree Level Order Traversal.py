# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Use collections.deque as queue.
        Cache the length of the current queue as the size of current level, so we 
        don't need a new list to separate the current level and the next one.
        '''
        if not root:
            return []
        queue = deque([root])
        values = []
        while queue:
            currentLevel = []
            currentLevelLen = len(queue)
            for _ in range(currentLevelLen):
                node = queue.popleft()
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(currentLevel)
        return values