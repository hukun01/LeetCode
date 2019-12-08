# 109. Convert Sorted List to Binary Search Tree
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        Top-down approach requires more time because we traverse the list multiple times.
        Build the tree from bottom up. We know the leftmost tree node in inorder traversal
        is the head of current list. So we can build the tree in inorder recursion, with
        boudaries info to each recursion call.
        '''
        listLen = 0
        node = head
        while node:
            listLen += 1
            node = node.next
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(0)
            root.left = build(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = build(mid + 1, right)
            return root
        return build(1, listLen)