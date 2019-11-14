# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        '''
        We can use a dict to cache all the (node, canRob) entries, but that
        would require us to traverse the nodes twice.
        A better approach is to have the recursive method return a tuple.
        In the tuple, the first element records the money we got by not robbing
        the current node; the second element records the money we got by
        robbing the current node. Then we only visit each node once.
        '''
        def robWithSelection(node):
            if not node:
                return 0, 0
            skipLeft, robLeft = robWithSelection(node.left)
            skipRight, robRight = robWithSelection(node.right)
            
            robNode = skipLeft + skipRight + node.val
            skipNode = max(robLeft, skipLeft) + max(robRight, skipRight)
            
            return skipNode, robNode
        return max(robWithSelection(root))