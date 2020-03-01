"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        Recursive - inorder traversal

        head = prev = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nonlocal prev, head
            if prev:
                prev.right = node
                node.left = prev
            prev = node
            if not head:
                head = prev
            inorder(node.right)
            
        inorder(root)
        if head:
            head.left = prev
            prev.right = head
        return head
        '''
        if not root:
            return None
        stack = []
        def pushLeft(node):
            while node:
                stack.append(node)
                node = node.left
        pushLeft(root)
        head = None
        prev = None
        while stack:
            cur = stack.pop()
            if not head:
                head = cur
            if prev:
                prev.right = cur
            cur.left = prev
            prev = cur
            pushLeft(cur.right)
        prev.right = head
        head.left = prev
        return head