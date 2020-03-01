# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        Scan through the tree, when going left, subtract pos by 1; when going right, add pos by 1.
        Use a dict to track the pos:[vals] mapping, finally convert the dict to list.
        Note that we can leverage collections.defaultdict(list), and
        use minPos and maxPos to track the boundaries to avoid sorting the dict at the end.
        '''
        ans = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        minPos = maxPos = 0
        while queue:
            node, pos = queue.popleft()
            if node is None:
                continue
            minPos = min(minPos, pos)
            maxPos = max(maxPos, pos)
            ans[pos].append(node.val)
            queue += [(node.left, pos-1), (node.right, pos+1)]
        return [] if len(ans) == 0 else [ans[i] for i in range(minPos, maxPos+1)]