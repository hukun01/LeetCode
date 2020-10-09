# 1586. Binary Search Tree Iterator II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    '''
    Stack + list.
    Use stack to iterate forward, record all visited values, and use it to
    iterate backward.
    '''

    def __init__(self, root: TreeNode):
        self.stack = []
        self.populateLeft(root)
        self.idx = -1 # idx of the current value
        self.vals = []
        
    def populateLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.vals) or self.stack

    def next(self) -> int:
        self.idx += 1
        if self.idx == len(self.vals):
            node = self.stack.pop()
            self.vals.append(node.val)
            self.populateLeft(node.right)
        return self.vals[self.idx]

    def hasPrev(self) -> bool:
        return self.idx > 0

    def prev(self) -> int:
        self.idx -= 1
        return self.vals[self.idx]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()