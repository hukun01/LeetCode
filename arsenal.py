'''
A collection of useful data structures.
'''

'''
One-dimensional binary indexed tree. An optional initialize() is provided
to initialize the tree in O(n) time.
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
        return i & (-i)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
            i += self.low_bit(i)

    def getPrefixSum(self, i):
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= self.low_bit(i)
        return ans

'''
A sliding window that maintains the current minimum.
In every iteration, user is supposed to call pop_expired() before calling min().
'''
class MinQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def push(self, x, pos):
        while self.queue and self.queue[-1][0] >= x:
            self.queue.pop()
        self.queue.append([x, pos])

    def pop_expired(self, pos):
        if self.queue and pos - self.queue[0][1] > self.size:
            self.queue.popleft()

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

    def union(self, x, y):
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parents[y] = x
        self.size[x] += self.size[y]
        self.component_count -= 1

    # return true if two are newly unioned, false if already unioned.
    def find_and_union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 != y0:
            self.union(x0, y0)
            return True
        return False