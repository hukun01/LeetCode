# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        '''
        Find the nodes right before 'left', reverse the sublist between those two nodes.
        Do it in one pass.
        '''
        dummy = cur = ListNode(next=head)
        pos = 1
        while pos <= left:
            if pos < left:
                cur = cur.next
                pos += 1
                continue
            
            # start reversing the sublist
            # at the end of this i need to have the node after right (can be None)
            # and connect the node before the sublist to the new head (the last node from the right).
            newTail = rPrev = cur.next
            rCur = rPrev.next
            for _ in range(right - left):
                rNext = rCur.next
                rCur.next = rPrev
                rPrev, rCur = rCur, rNext

            newHead = rPrev
            cur.next = newHead
            newTail.next = rCur
            break
        
        return dummy.next
