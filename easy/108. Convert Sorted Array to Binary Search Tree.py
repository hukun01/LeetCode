# 108. Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid+1, right)
            return root
        return build(0, len(nums) - 1)
        '''
        2/2 Iterative is based on the above recursive approach.
        The key is to push the (root, left, right, isLeft) tuple to stack.
        '''
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        stack = [(root, 0, mid - 1, True), (root, mid + 1, right, False)]
        while stack:
            node, left, right, isLeft = stack.pop()
            if left <= right:
                mid = (left + right) // 2
                newNode = TreeNode(nums[mid])
                if isLeft:
                    node.left = newNode
                else:
                    node.right = newNode
                stack.append((newNode, left, mid - 1, True))
                stack.append((newNode, mid + 1, right, False))
        return root