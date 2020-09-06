# 1562. Find Latest Group of Size M
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        '''
        1/3 Simplified union find.
        Track the lengths of all intervals, with left and right ends being the
        keys. When merging intervals, only update the current point and its
        left and right ends.
        '''
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
        return res

        '''
        2/3 Straightforward union find.
        '''
        arr = [i - 1 for i in arr]
        n = len(arr)
        uf = UnionFind(n)
        s = ['0'] * n
        steps = -1
        if m == 1:
            steps = 1
        for i, idx in enumerate(arr):
            s[idx] = '1'
            uf.sz_count[1] += 1
            if idx > 0 and s[idx-1] == '1':
                uf.find_and_union(idx, idx-1)
            if idx < n-1 and s[idx+1] == '1':
                uf.find_and_union(idx, idx+1)
            if uf.sz_count[m] > 0:
                steps = i + 1
        return steps

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

    '''
    3/3 Max sliding window.
    Same as 683. K Empty Slots
    '''
        n = len(arr)
        if n == m:
            return n
        bit_to_step = [0] * n
        for step, bit in enumerate(arr):
            bit_to_step[bit-1] = step + 1
        ans = -1
        max_q = MaxQueue(m)
        for bit, step in enumerate(bit_to_step):
            max_q.pop_expired(bit)
            max_q.push(step, bit)
            if bit + 1 < m: # since bit starts from 0, we need to adjust it.
                continue
            left = right = math.inf
            if bit - m >= 0:
                left = bit_to_step[bit-m]
            if bit + 1 < n:
                right = bit_to_step[bit+1]
            if max_q.max() < (d := min(left, right)):
                ans = max(ans, d - 1)
        return ans

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