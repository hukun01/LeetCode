# 1825. Finding MK Average
class MKAverage:
    '''
    1/2 Binary Indexed Tree.

    We need to quickly find the sum of an interval whose elements are getting
    added at the same time. BIT is a good data structure to achieve that.

    Use two BITs, one tracks the number frequency, another tracks the number
    values.
    Use the freq BIT to find the indices of the prefix freq sums that have 'k'
    and 'm - k' numbers, respectively. Note that the freq indices here will be
    the actual values at the [k:m-k] boundaries, 'lo' and 'hi'.
    Then use value BIT to get the prefix sum of BIT[:lo] and BIT[:hi], from
    which we can find the sum of BIT[lo:hi].

    However, the sum of BIT[lo:hi] is not yet accurate, because if there are
    multiple numbers on the boundaries, we would have added/subtracted too much.
    On the boundary lo, we need to add back (freq.prefix_sum(lo) - k) * lo;
    On the boundary hi, we need to remove (freq.prefix_sum(hi) - (m - k)) * hi;

    Time: O(log(n)), O(log(n)) for calculateMKAverage and addElement, where n
          is the upper bound of the data range.
    Space: O(n)
    '''
    _UPPER_BOUND = 10 ** 5 + 1

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k 
        self.data = deque()
        self.value = BinaryIndexedTree(MKAverage._UPPER_BOUND)
        self.freq = BinaryIndexedTree(MKAverage._UPPER_BOUND)

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.value.add(num, num)
        self.freq.add(num, 1)
        if len(self.data) > self.m: 
            num = self.data.popleft()
            self.value.add(num, -num)
            self.freq.add(num, -1)

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m:
            return -1 
        lo = self.freq.find_index(self.k)
        hi = self.freq.find_index(self.m - self.k)
        ans = self.value.get_prefix_sum(hi) - self.value.get_prefix_sum(lo)
        ans += (self.freq.get_prefix_sum(lo) - self.k) * lo
        ans -= (self.freq.get_prefix_sum(hi) - (self.m-self.k)) * hi
        return ans // (self.m - 2*self.k)


class BinaryIndexedTree:
    def __init__(self, n):
        self.nums = [0] * (n + 1)

    def _low_bit(self, i):
        '''
        Isolate the last bit from i.
        '''
        return i & (-i)

    def add(self, i, val):
        '''
        Add the frequency at index i by val.
        '''
        while i < len(self.nums):
            self.nums[i] += val
            i += self._low_bit(i)

    def find_index(self, k):
        '''
        Quickly find the lower bound index at which the prefix sum >= k. This
        takes O(log(n)) time, see https://codeforces.com/blog/entry/61364.

        This only works if the prefix sums are monotoically non-decreasing.
        Otherwise, need to use binary search to find the index, which takes
        O((log(n))^2) time.
        '''
        total = 0
        pos = 0
        n = len(self.nums)
        for i in range(int(log(n, 2)), -1, -1):
            if pos + (1 << i) < n and total + self.nums[pos + (1 << i)] < k:
                pos += (1 << i)
                total += self.nums[pos]
        return pos + 1

    def get_prefix_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.nums[i]
            i -= self._low_bit(i)
        return ans


class MKAverage:
    '''
    2/2 Heaps.

    arr:    [a0, a1, a2, a3, a4, a5, a6]
    right1:                     [a5, a6]
    left1:  [a0, a1, a2, a3, a4]
    right2:         [a2, a3, a4, a5, a6]
    left2:  [a0, a1]

    Similar to 480. Sliding Window Median
    '''

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.arr = [0]*m
        self.left1 = [(0, i) for i in range(m - k)]
        self.right1 = [(0, i) for i in range(m - k, m)]
        self.left2 = [(0, i) for i in range(k)]
        self.right2 = [(0, i) for i in range(k, m)]
        heapify(self.left1)
        heapify(self.right1)
        heapify(self.left2)
        heapify(self.right2)
        self.score = 0

    def update(self, left, right, m, k, num):
        score, T = 0, len(self.arr)
        if num > left[0][0]:
            heappush(left, (num, T))        
            if self.arr[T - m] <= left[0][0]:
                if left[0][1] >= T - m: score += left[0][0]
                score -= self.arr[T - m]
                heappush(right, (-left[0][0], left[0][1]))
                heappop(left)
        else:
            heappush(right, (-num, T))       
            score += num
            if self.arr[T - m] >= left[0][0]: 
                heappush(left, (-right[0][0], right[0][1]))
                q = heappop(right)
                score += q[0]
            else:
                score -= self.arr[T - m]

        while right and right[0][1] <= T - m: heappop(right)  # lazy-deletion
        while left and left[0][1] <= T - m: heappop(left)  # lazy-deletion
        return score

    def addElement(self, num):
        t1 = self.update(self.left1, self.right1, self.m, self.k, num)
        t2 = self.update(self.left2, self.right2, self.m, self.m - self.k, num)
        self.arr.append(num)
        self.score += (t2 - t1)

    def calculateMKAverage(self):
        if len(self.arr) < 2*self.m: return -1
        return self.score//(self.m - 2*self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()