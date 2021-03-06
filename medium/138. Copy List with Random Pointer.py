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
        if not head:
            return None

        # Create the shadow list
        curr = head
        while curr:
            clone = Node(curr.val, curr.next, None)
            curr.next = clone
            curr = curr.next.next
        
        # Copy the random pointer
        curr = head
        while curr and curr.next:
            clone = curr.next
            if curr.random:
                clone.random = curr.random.next
            curr = curr.next.next

        # Separate out the two lists
        cached = head.next
        curr = head
        while curr:
            clone = curr.next
            curr.next = clone.next
            curr = curr.next
            if curr:
                clone.next = curr.next
        return cached
        '''
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapping = {None: None}
        node = head
        while node:
            mapping[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            mapping[node].next = mapping[node.next]
            mapping[node].random = mapping[node.random]
            node = node.next
        return mapping[head]
        '''