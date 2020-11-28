# 327. Count of Range Sum
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        General direction is based on below naive process.
        for j in range(n + 1):
            for i in range(j):
                if lower <= sum_j - sum_i <= upper: ans += 1

        This process can be transformed into another:
        for j in range(n + 1):
            sum_i_count = number of sum_i such that sum_j - upper <= sum_i <= sum_j - lower
            ans += sum_i_count

        Now we have an outer loop with O(n), the key is to get sum_i_count faster.
        Below are the 2 ways to achieve this.
        Time: O(nlog(n)) where n is the length of nums.
        Space: O(n)
        '''
        '''
        1/2 SortedList.
        We use a SortedList to keep the sum_j's, and find 'sum_j - lower' and
        'sum_j - upper' in O(log(n)) time.
        '''
        from sortedcontainers import SortedList
        ans = 0
        sum_j = 0
        sorted_presums = SortedList([0])
        for a in nums:
            sum_j += a
            idx_l = sorted_presums.bisect_left(sum_j - upper)
            idx_r = sorted_presums.bisect_right(sum_j - lower)
            sum_i_count = idx_r - idx_l
            ans += sum_i_count
            sorted_presums.add(sum_j)            
        return ans
        '''
        2/2 Fenwick tree, Binary Indexed Tree (BIT).
        As using sortedcontainers is kinda cheating, we often need to go down
        the path employing a BIT, to do the same thing.
        Here we compute the whole presums first, and keep a sorted copy of it.
        Use a BIT to keep track of the frequencies of the indicies of 
        'sum_j - lower' and 'sum_j - upper', then 'sum_i_count' is the
        frequency diff between these two indicies.
        Note as BIT doesn't use index 0, when adding sum_j's index we need to
        add 1 to it.
        '''
        presums = [0] + list(itertools.accumulate(nums))
        tree = BinaryIndexedTree(len(presums))
        ans = 0
        sorted_presums = sorted(presums)
        for sum_j in presums:
            idx_l = bisect_right(sorted_presums, sum_j - lower)
            idx_r = bisect_left(sorted_presums, sum_j - upper)
            sum_i_count = tree.get(idx_l) - tree.get(idx_r)
            ans += sum_i_count
            idx = bisect_left(sorted_presums, sum_j) + 1
            tree.add(idx, 1)
        return ans

class BinaryIndexedTree:
    def __init__(self, n):
        self.data = [0] * (n + 1)
    
    def _low_bit(self, x):
        return -x & x
    
    def add(self, i, val):
        while i < len(self.data):
            self.data[i] += val
            i += self._low_bit(i)
    
    def get(self, i):
        ans = 0
        while i > 0:
            ans += self.data[i]
            i -= self._low_bit(i)
        return ans