# 430. Flatten a Multilevel Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        prev = None
        cached_nexts = []
        while node or cached_nexts:
            if not node:
                node = cached_nexts.pop()
                continue
            if prev:
                prev.next = node
                node.prev = prev
            prev = node
            if node.child:
                cached_nexts.append(node.next)
                node.next = node.child
                node.child = None
            node = node.next
        return head