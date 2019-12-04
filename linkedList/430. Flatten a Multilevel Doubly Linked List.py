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
        cachedNexts = []
        while node:
            if node.child:
                cachedNexts.append(node.next) # cache the most recent next before entering child list
                node.next = node.child
                node.child.prev = node
                node.child = None
            elif not node.next and cachedNexts:
                node.next = cachedNexts.pop() # return to the parent list's next
                if node.next:
                    node.next.prev = node
            node = node.next
        return head