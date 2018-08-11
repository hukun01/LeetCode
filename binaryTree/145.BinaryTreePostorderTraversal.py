# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        Morris traversal. Similar to InOrder traversal. 
        Key is to use a dummy node whose left child is root! Also need to reverse the
        whole right linked list when accessing.

        :type root: TreeNode
        :rtype: List[int]
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