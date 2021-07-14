# 1586. Binary Search Tree Iterator II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    '''
    Two stacks.
    The key is to not store all visited values in a list, as that defeats the
    purpose of an iterator.

    Use two stacks, one for next nodes, one for previous nodes.
    A KEY is: when calling prev(), pop the prev_stack node and push it to the
    next_stack, so we can take the node from the next_stack in the future calls
    to next().
    Anothe KEY is in prev(), take the last from 'prev_stack', AFTER poping it
    out, this ensures we take the previous element, not the one we just visited
    which is considered the current element.
    Note that as we push left chain into next_stack, when mixing with previous
    node, we need to avoid pushing left chain more than once. We add a flag to
    the stack entry called 'from_prev' meaning whether the node in next_stack
    is from prev_stack, if so, we don't push left chain from this node, as it
    must have been pushed before when calling next().

    Time: O(n) where n is number of nodes.
    Space: O(h) where h is tree height.
    '''

    def __init__(self, root: TreeNode):
        self.next_stack = []
        self.prev_stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        while node:
            self.next_stack.append((node, False)) # (node, right_visited)
            node = node.left

    def hasNext(self) -> bool:
        return len(self.next_stack) > 0

    def next(self) -> int:
        node, right_visited = self.next_stack.pop()
        if not right_visited:
            self._push_left(node.right)

        self.prev_stack.append(node)
        return node.val

    def hasPrev(self) -> bool:
        return len(self.prev_stack) > 1

    def prev(self) -> int:
        self.next_stack.append((self.prev_stack.pop(), True))
        return self.prev_stack[-1].val


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()