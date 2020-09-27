# 708. Insert into a Sorted Circular Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        '''
        Control flow.
        Use two pointers, prev and curr, to locate the insert position.
        There are 3 cases:
        1. Insert in the middle;
        2. Insert after the tail if the value is the biggest. This is the same
           as inserting before the head;
        3. All existing values are the same, and we can insert the new value anywhere.
        '''
        if head == None:
            new = Node(insertVal, None)
            new.next = new
            return new
 
        prev, curr = head, head.next
        toInsert = False
        while True:
            if prev.val <= insertVal <= curr.val:
                # Case #1: insert the value in the middle.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2: didn't find any position for insert value in the middle.
                # Now locate the tail element with 'prev', see if we can insert it
                # at the tail, aka, before the start.
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                break

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break

        prev.next = Node(insertVal, curr)
        return head