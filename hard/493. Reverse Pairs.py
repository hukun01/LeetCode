# 493. Reverse Pairs
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        1/2 Using SortedList from sortedcontainers module.

        Similar to 315. Count of Smaller Numbers After Self
        '''
        from sortedcontainers import SortedList
        seen = SortedList()
        ans = 0
        for j, num_j in enumerate(nums):
            i = seen.bisect_right(num_j * 2)
            ans += j - i
            seen.add(num_j)
        return ans

        '''
        2/2. Fenwick tree/Binary Indexed Tree.
        A trick here is to convert the original numbers into relative
        ranks, this is to avoid making the BIT's array too big.

        Similar to 315. Count of Smaller Numbers After Self
        '''
        num_to_rank = { v: i for i, v in enumerate(
            sorted(set(nums + [2*a for a in nums])), start = 1) }
        tree = BinaryIndexedTree(len(num_to_rank))
        ans = 0
        for j, num_j in enumerate(nums):
            i = tree.getPrefixSum(num_to_rank[num_j * 2])
            ans += j - i
            tree.update(num_to_rank[num_j], 1)
        return ans

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