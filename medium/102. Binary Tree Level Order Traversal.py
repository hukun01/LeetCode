# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        Use collections.deque as queue.
        Cache the length of the current queue as the size of current level, so we 
        don't need a new list to separate the current level and the next one.

        :type root: TreeNode
        :rtype: List[List[int]]
        """
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