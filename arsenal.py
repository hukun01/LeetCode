'''
A collection of useful data structures.
'''

'''
One-dimensional binary indexed tree. An optional initialize() is provided
to initialize the tree in O(n) time.

See more in https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
'''
class BinaryIndexedTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    # O(n) initialization. Better than using update() which leads to O(Ologn).
    def initialize(self, nums):
        assert len(nums) + 1 == len(self.sums)

        for i, a in enumerate(nums, start = 1):
            self.sums[i] += a
            if (parent_idx := i + self.low_bit(i)) <= len(nums):
                self.sums[parent_idx] += self.sums[i]

    def low_bit(self, i):
        '''
        Isolate the last bit from i.
        '''
        return i & (-i)

    def update(self, i, val):
        '''
        Add the frequency at index i by val.
        '''
        while i < len(self.sums):
            self.sums[i] += val
            i += self.low_bit(i)

    def get_prefix_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= self.low_bit(i)
        return ans

class BinaryIndexedTree2D:
    '''
    The main difference between 1D and 2D BITs is that, in 2D, for every 'r',
    we need to update/query all 'c', in a nested loop. Similar logic applies
    to more dimensions.
    '''
    def __init__(self, r, c):
        self.data = [[0] * (c + 1) for _ in range(r + 1)]
        self.R = r + 1
        self.C = c + 1

    def low_bit(self, i):
        '''
        Isolate the last bit from i.
        '''
        return i & (-i)
    
    def update(self, r, c, v):
        while r < self.R:
            self.update_c(r, c, v)
            r += self.low_bit(r)
            
    def update_c(self, r, c, v):
        while c < self.C:
            self.data[r][c] += v
            c += self.low_bit(c)
    
    def query(self, r, c):
        ans = 0
        while 0 < r:
            ans += self.query_c(r, c)
            r -= self.low_bit(r)
        return ans
    
    def query_c(self, r, c):
        ans = 0
        while 0 < c:
            ans += self.data[r][c]
            c -= self.low_bit(c)
        return ans

'''
A sliding window that maintains the current maximum.
In every iteration, user is supposed to call pop_expired() before calling max().
'''
class MaxQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def pop_expired(self, pos):
        if self.queue and pos - self.queue[0][1] >= self.size:
            self.queue.popleft()

    def push(self, x, pos):
        while self.queue and self.queue[-1][0] <= x:
            self.queue.pop()
        self.queue.append([x, pos])

    def max(self):
        return self.queue[0][0]

'''
A sliding window that maintains the current minimum.
In every iteration, user is supposed to call pop_expired() before calling min().
'''
class MinQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def pop_expired(self, pos):
        if self.queue and pos - self.queue[0][1] >= self.size:
            self.queue.popleft()

    def push(self, x, pos):
        while self.queue and self.queue[-1][0] >= x:
            self.queue.pop()
        self.queue.append([x, pos])

    def min(self):
        return self.queue[0][0]

'''
Array based union find with path compression and rank based union.
Need the count of nodes to initialize.
Usually to apply UF in a 2d matrix, user can write a get_id(r, c) to compute
the unique id of each position in the 2d matrix.
'''
class UnionFind:
    def __init__(self, n):
        self.component_count = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # return true if two are newly unioned, false if already unioned.
    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return False
        if self.size[x0] < self.size[y0]:
            x0, y0 = y0, x0
        self.parents[y0] = x0
        self.size[x0] += self.size[y0]
        self.component_count -= 1
        return True


class SegTreeNode:
    '''
    Segment Tree with lazy propagation.
    In general, a segment tree handles range operations:
    1. Range queries: range minimum/maximum query (RMQ), range sum query (RSQ)
    2. Range update (with lazy propagation)

    Also, single point update and single point query is supported via range of
    size 1.

    This particular template handles range sum query. For RMQ it can be updated
    accordingly.

    For general intro and lazy propagation see:
    https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
    For discretization, see 218. The Skyline Problem.
    '''
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

    def update_range(self, a, b, val):
        # Update is applied to the first node that completely covered by
        # [a, b], this way we don't go to each leaf node, and achieve
        # O(log(n)) time range update.
        if self.a >= a and self.b <= b:
            self.lazy += val * (self.b - self.a + 1)
            return

        if a > self.b or b < self.a or self.a == self.b:
            return

        self.left.update_range(a, b, val)
        self.right.update_range(a, b, val)
    
    def query_range(self, a):
        # When querying, we need to push down lazy value from upper nodes to
        # bottom nodes. Note that we need to split the lazy values from the
        # parent node to its children nodes based on each child's size.
        if self.left is None:
            self.val += self.lazy
            self.lazy = 0
            if a == self.a: # if true, it also means self.a == self.b
                return self.val
            return 0

        if b < self.a or a > self.b:
            return 0

        if self.lazy != 0:
            self.left.lazy += self.lazy * (self.left.b - self.left.a + 1) // (self.b - self.a + 1)
            self.right.lazy += self.lazy * (self.right.b - self.right.a + 1) // (self.b - self.a + 1)
            self.lazy = 0

        return self.left.query_range(a, b) + self.right.query_range(a, b)