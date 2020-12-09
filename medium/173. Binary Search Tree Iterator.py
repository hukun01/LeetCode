# 173. Binary Search Tree Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushLeftSubTree(root)

    def next(self) -> int:
        last = self.stack.pop()
        self.pushLeftSubTree(last.right)
        return last.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def pushLeftSubTree(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())