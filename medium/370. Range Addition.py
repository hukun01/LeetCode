# 370. Range Addition
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        1/2 Difference array.
        This is the inverse of prefix sums:  diff[i] = nums[i] - nums[i - 1].
        Based on this we know: 
            1. nums[i] = diff[i] + nums[i - 1]
            2. nums[0] = diff[0]
        Then we can get nums by accumulating diff.

        The diff array first collects the start and end positions for each
        udpate interval, and record the delta, by adding `delta` to start,
        and minus `delta` to (end+1). Later we accumulate diff array, the
        `delta` in start will be accumulated to every position after it,
        until (end+1), after which the accumulated `delta` will be negated.

        Difference array provides O(1) update to any intervals in an array,
        with the cost of O(n) query. Hence, this technique is often used in
        scenarios where frequent update operations are applied to various
        intervals, and our goal is to get the result array AFTER all the
        operations.

        Time: O(length)
        Space: O(length)
        '''
        diff = [0] * (length + 1)
        for s, e, inc in updates:
            diff[s] += inc
            diff[e + 1] -= inc
        return list(accumulate(diff[:-1]))
        '''
        2/2 Segment Tree. See arsenal.py file for more Segment Tree details.
        '''
        root = SegTreeNode(0, length-1)
        root.init(0, length-1)
        for s, e, inc in updates:
            root.update_range(s, e, inc)

        return [root.query_range(i, i) for i in range(length)]


class SegTreeNode:
    def __init__(self, a, b):
        # This node covers interval [a, b] inclusively.
        self.a = a
        self.b = b
        self.left = self.right = None
        self.val = 0
        self.lazy = 0


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
        if self.lazy == 0:
            return
        self.left.val += self.lazy * self.left.size()
        self.right.val += self.lazy * self.right.size()
        self.left.lazy += self.lazy
        self.right.lazy += self.lazy
        self.lazy = 0


    def update_range(self, a, b, val):
        if a > self.b or b < self.a:
            return

        # Update is applied to the first node that completely covered by
        # [a, b], this way we don't go to each leaf node, and achieve
        # O(log(n)) time range update.
        if self.a >= a and self.b <= b:
            self.val += val * self.size()
            self.lazy += val
            return

        self.propagate_lazy()

        self.left.update_range(a, b, val)
        self.right.update_range(a, b, val)


    def query_range(self, a, b):
        if a > self.b or b < self.a:
            return 0

        if self.a >= a and self.b <= b:
            return self.val

        self.propagate_lazy()

        return self.left.query_range(a, b) + self.right.query_range(a, b)


    def size(self):
        return self.b - self.a + 1