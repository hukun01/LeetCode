# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        Note that 1..n is the in-order traversal for any BST with nodes 1 to n. 
        So if I pick i-th node as my root, the left subtree will contain 
        elements 1 to (i-1), and the right subtree will contain 
        elements (i+1) to n. I use recursive calls to get back all possible trees 
        for left and right subtrees and combine them in all possible ways with the root.
        '''
        def make(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                lefts = make(start, i - 1)
                rights = make(i + 1, end)
                
                for left in lefts:
                    for right in rights:
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res
        
        if n == 0:
            return []
        return make(1, n)