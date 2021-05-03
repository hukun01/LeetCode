# 314. Binary Tree Vertical Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        BFS.

        Scan through the tree, when going left, subtract pos by 1; when going
        right, add pos by 1.
        Use a dict to track the pos:[vals] mapping, finally convert the dict to
        list.

        Note that we can record the min_pos and max_pos to track the boundaries
        to avoid sorting the dict at the end.
        Also, the reason for BFS is because we want to return the nodes from
        the earlier levels first, if they are on the same column.

        Time: O(n) where n is the number of tree nodes.
        Space: O(n)
        '''
        ans = defaultdict(list)
        queue = deque([(root, 0)])
        min_pos = max_pos = 0
        while queue:
            node, pos = queue.popleft()
            if node is None:
                continue
            min_pos = min(min_pos, pos)
            max_pos = max(max_pos, pos)
            ans[pos].append(node.val)
            queue += [(node.left, pos-1), (node.right, pos+1)]

        return [] if len(ans) == 0 else [ans[i] for i in range(min_pos, max_pos+1)]