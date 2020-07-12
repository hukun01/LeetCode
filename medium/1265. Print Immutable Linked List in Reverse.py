# 1265. Print Immutable Linked List in Reverse
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        '''
        Sqrt decomposition.
        O(n) time and space is trivial (cache all results and reverse them).
        Sqrt decomposition achieves O(n^(1/2)) space and O(n) time.
        
        Get the size of linked list in O(n) time.
        Split the linked list into n^(1/2) sublist each with n^(1/2) nodes,
        this takes O(n) time and O(n^(1/2)) space.
        Reversely, using each sublist head, use the trivial method to
        reversely print the sublist with O(n^(1/2)) space and time.
        '''
        def getLinkedListSize(head):
            size = 0
            while head:
                size += 1
                head = head.getNext()
            return size
        def printLinkedListInReverseDirect(head, size):
            if size and head:
                printLinkedListInReverseDirect(head.getNext(), size-1)
                head.printValue()
        
        size = getLinkedListSize(head)
        
        num_blocks = math.ceil(math.sqrt(size))
        block_size = math.ceil(size / num_blocks)
        
        blocks = []
        for cur in range(size):
            if cur % block_size == 0:
                blocks.append(head)
            head = head.getNext()
        
        while blocks:
            printLinkedListInReverseDirect(blocks.pop(), block_size)