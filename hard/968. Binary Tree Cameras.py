# 968. Binary Tree Cameras
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        '''
        1/2
        Post-order traversal.
        
        Use a set to keep track of the covered nodes, and add a camera to the node
        that is not covered.
        
        Go to the bottom of the tree, if any of the node's children is not covered,
        we need a camera on the node;
        Or if the node is not covered and its parent is None, we also need a camera
        on it, this can only be true for the root node.
        
        Note that we need to initialize the covered set with { None } because emtpy
        child should be considered covered already.
        '''
        ans = 0
        covered = { None }
        def dfs(parent, node):
            if not node:
                return
            dfs(node, node.left)
            dfs(node, node.right)
            
            if (parent is None and node not in covered) or\
                node.left not in covered or\
                node.right not in covered:
                nonlocal ans
                ans += 1
                covered.update({ parent, node, node.left, node.right })
        dfs(None, root)
        return ans

        '''
        2/2
        We will have to cover leaf nodes, and there are 2 options for that:
        1. put a camera on the leaf node;
        2. put a camera on the leaf node's parent.
        Option 2 is always at least as good as option 1, so we should always do option 2.
        
        With a recursive method traversing the tree, there are 3 statuses we need to handle:
        1. return 0 if it's a leaf, meaning that it needs to be covered by the parent;
        2. return 1 if it's a parent of a leaf, it must have a camera;
        3. return 2 if it's covered without a camera.


        ans = 0
        def dfs(node):
            if not node:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                nonlocal ans
                ans += 1
                return 1
            return 2 if left == 1 or right == 1 else 0
        if dfs(root) == 0:
            ans += 1
        return ans
        '''