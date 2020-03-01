# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """ 1/2 Recursive
        def buildTree(nums, left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = buildTree(nums, left, mid - 1)
            root.right = buildTree(nums, mid + 1, right)
            return root
        return buildTree(nums, 0, len(nums) - 1)
        """
        """  2/2 Iterative is based on the above recursive approach. The key is to push the (root, left, right, isLeft) tuple.
        """
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        stack = [(root, 0, mid - 1, True), (root, mid + 1, right, False)]
        while stack:
            node, left, right, isLeft = stack.pop()
            if left <= right:
                mid = left + (right - left) // 2
                newNode = TreeNode(nums[mid])
                if isLeft:
                    node.left = newNode
                else:
                    node.right = newNode
                stack.append((newNode, left, mid - 1, True))
                stack.append((newNode, mid + 1, right, False))
        return root