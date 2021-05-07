# 109. Convert Sorted List to Binary Search Tree
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        Build tree using inorder (inorder traversal is highly related to BST)

        Time: O(N)
        Space: O(log(N)), if not counting TreeNode creation space
        '''
        self.node = head
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            left = build(l, m-1)
            root = TreeNode(self.node.val, left=left)

            '''
            Every time when we create a new TreeNode which uses node.val, we
            move the node to the next. whenever we are done building the left
            sub tree, we should have created (mid - left - 1) nodes, then the
            head will point to the middle node.
            '''
            self.node = self.node.next

            root.right = build(m+1, r)
            return root

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        return build(1, n)