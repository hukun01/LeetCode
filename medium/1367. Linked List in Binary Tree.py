# 1367. Linked List in Binary Tree
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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        '''
        KMP on tree.
        Build the lps table for linked list, then use it to match with tree.

        Time: O(n + m) where n is len(list), m is len(tree)
        Space: O(n + h) where h is tree height
        '''
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def build_lps(s):
            n = len(s)
            lps = [0] * n
            for i in range(1, n):
                k = lps[i - 1]
                while k > 0 and s[k] != s[i]:
                    k = lps[k - 1]

                if s[k] == s[i]:
                    lps[i] = k + 1

            return lps

        lps = build_lps(arr)

        def dfs(node, i):
            if not node:
                return False
            while i > 0 and node.val != arr[i]:
                i = lps[i - 1]

            if node.val == arr[i]:
                i += 1

            return i == len(arr) or dfs(node.left, i) or dfs(node.right, i)

        return dfs(root, 0)