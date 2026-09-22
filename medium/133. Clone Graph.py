"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Recursion. We need to clone each node and treat
        its neighbors the same way, so use recursion on each neighbor.
        Use a mapping to avoid duplicate clones.
        '''
        cloned = {}
        def clone(cur):
            if not cur:
                return None
            if cur not in cloned:
                newNode = Node(cur.val, [])
                cloned[cur] = newNode
                for nei in cur.neighbors:
                    newNode.neighbors.append(clone(nei))
            
            return cloned[cur]
            
        return clone(node)
