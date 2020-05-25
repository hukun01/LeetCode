# 1008. Construct Binary Search Tree from Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        '''
        DFS.
        Based on the preorder attribute, the first node would be the root of
        the (sub)tree. And its left subtree's values range would be upper bounded by
        the root val. When going into the left subtree, the lower bound would be
        the that from the previous level of recursion. Similar logic applies to
        processing the right subtree.
        '''
        def dfs(q, upper, lower):
            if not q or q[0] < lower or q[0] > upper:
                return None
            node = TreeNode(q.popleft())
            node.left = dfs(q, lower, node.val)
            node.right = dfs(q, node.val, upper)
            return node
        return dfs(deque(preorder), -math.inf, math.inf)