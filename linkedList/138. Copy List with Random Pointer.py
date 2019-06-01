"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        Method 1: Use a dict to track the mappings between existing nodes and clones, and build the links;
        Method 2: Create a shadow list, change existing n1->n2->n3 to n1->clone1->n2->clone2->n3->clone3,
        and build the links, and then restore the 2 lists.
        '''
        dummy = curr = head
        while curr:
            clone = Node(curr.val, curr.next, None)
            curr.next = clone
            curr = curr.next.next
        curr = head
        while curr and curr.next:
            clone = curr.next
            if curr.random:
                clone.random = curr.random.next
            else:
                clone.random = None
            curr = curr.next.next
        curr = head
        while curr:
            clone = curr.next
            curr.next = clone.next
            curr = curr.next
            clone.next = curr.next if curr else None
        return dummy.next
        '''
    def copyRandomList(self, head: 'Node') -> 'Node':
        mappings = dict()
        curr = head
        while curr:
            clone = Node(curr.val, None, None)
            mappings[curr] = clone
            curr = curr.next
        curr = head
        while curr:
            clone = mappings[curr]
            clone.next = mappings[curr.next] if curr.next else None
            clone.random = mappings[curr.random] if curr.random else None
            curr = curr.next
        return mappings[head] if mappings else None
        '''