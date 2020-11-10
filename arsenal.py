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