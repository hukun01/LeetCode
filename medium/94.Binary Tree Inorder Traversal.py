# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ''' 1/2 Iterative using stack: 
        To make the logic clear, use a nested function push_left_nodes()
        to push all the left children of one Node and itself into the stack.
        We push all the left children of root and root into the stack until there's no more nodes.
        Then we pop from the stack which we'd call cur. Add cur to result list.
        Iteratively call pushAllLeft() on cur's right child.
        '''
        stack = []
        ans = []
        def push_left_nodes(node, stack):
            while node:
                stack.append(node)
                node = node.left
        push_left_nodes(root, stack)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            push_left_nodes(node.right, stack)
        return ans
        ''' 2/2 Morris traversal: See 0.Notes.txt
        '''
        ans = []
        cur = root
        while cur:
            if cur.left:
                node = cur.left
                while node.right not in { None, cur }:
                    node = node.right

                if node.right == cur:
                    node.right = None
                    ans.append(cur.val)
                    cur = cur.right
                else:
                    node.right = cur
                    cur = cur.left
            else:
                ans.append(cur.val)
                cur = cur.right

        return ans