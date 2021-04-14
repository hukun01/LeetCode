# 699. Falling Squares
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        '''
        Segment Tree with discretization and lazy propagation.

        For each square, in its range [left, left + size - 1], we need to know
        the max, which can be answered by a segment tree.
        And the new height in this range would be updated to 'max + size',
        which can also be handled by the segment tree.
        In the meantime, we record the current max as part of the answer.

        Time: O(n log(n)) where n is len(positions)
        Space: O(n)
        '''
        pos2idx = {}
        pos = set()
        for a, size in positions:
            b = a + size - 1
            pos |= {a, b}

        i = 0
        pos = sorted(pos)
        for a in pos:
            pos2idx[a] = i
            i += 1

        n = len(pos)
        root = SegTreeNode(0, n-1)
        root.init(0, n-1)

        ans = []
        for a, size in positions:
            b = a + size - 1
            left = pos2idx[a]
            right = pos2idx[b]
            range_max = root.query_range_max(left, right)
            root.update_range(left, right, range_max + size)
            ans.append(root.val)

        return ans


class SegTreeNode:
    def __init__(self, a, b):
        # This node covers interval [a, b] inclusively.
        self.a = a
        self.b = b
        self.left = self.right = None
        self.val = 0
        self.lazy = False


    def __repr__(self):
        # This is for debug only
        return f'[{self.a, self.b}] with val {self.val} and lazy {self.lazy}\nleft: {self.left}\nright: {self.right}'

    def init(self, a, b):
        if a == b:
            return
        m = (a + b) // 2
        self.left = SegTreeNode(a, m)
        self.right = SegTreeNode(m + 1, b)
        self.left.init(a, m)
        self.right.init(m + 1, b)


    def propagate_lazy(self):
        if not self.lazy:
            return
        self.left.val = self.right.val = self.val
        self.left.lazy = self.right.lazy = self.lazy
        self.lazy = False


    def update_range(self, a, b, val):
        if a > self.b or b < self.a:
            return

        # Update is applied to the first node that completely covered by
        # [a, b], this way we don't go to each leaf node, and achieve
        # O(log(n)) time range update.
        self.val = max(self.val, val)

        if self.a >= a and self.b <= b:
            self.lazy = True
            return

        self.propagate_lazy()

        self.left.update_range(a, b, val)
        self.right.update_range(a, b, val)


    def query_range_max(self, a, b):
        if a > self.b or b < self.a:
            return 0

        if self.a >= a and self.b <= b:
            return self.val

        self.propagate_lazy()

        return max(self.left.query_range_max(a, b), self.right.query_range_max(a, b))