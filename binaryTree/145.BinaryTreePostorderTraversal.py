# 145. Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        1/2 Iterative approach using 1286's methodology.
        '''
        '''
        Recursive method as a refernce for finding entry points.

            def postorder(node):
                # entry0
                if not node:
                    return
                postorder(node.left)
                # entry1
                postorder(node.right)
                # entry2
                ans.append(node.val)
        '''
        ans = []
        stack = [(0, root)]
        def step():
            entry, node = stack.pop()
            if entry == 0:
                if not node:
                    return
                stack.append((1, node))
                stack.append((0, node.left))
            elif entry == 1:
                stack.append((2, node))
                stack.append((0, node.right))
            elif entry == 2:
                return node.val
            
        while stack:
            x = step()
            if x:
                ans.append(x)

        return ans

        """
        2/2 Morris traversal. Similar to InOrder traversal. 
        Key is to use a dummy node whose left child is root! Also need to reverse the
        whole right linked list when accessing.
        """
        def reverseLinkedList(start):
            prevHead = None
            while start:
                recordNext = start.right
                start.right = prevHead
                prevHead = start
                start = recordNext
        def accessLinkedList(start, values):
            while start:
                values.append(start.val)
                start = start.right
        values = []
        dummy = TreeNode(0)
        dummy.left = root
        cur = dummy
        while cur:
            if cur.left:
                node = cur.left
                while node.right != cur and node.right:
                    node = node.right
                if not node.right:
                    node.right = cur
                    cur = cur.left
                else:
                    node.right = None
                    reverseLinkedList(cur.left)
                    accessLinkedList(node, values)
                    reverseLinkedList(node)
                    cur = cur.right
            else:
                cur = cur.right
        return values