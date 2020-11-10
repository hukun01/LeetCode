# 1649. Create Sorted Array through Instructions
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        '''
        1/2 Using SortedList from sortedcontainers module.
        '''
        from sortedcontainers import SortedList
        MOD = 10 ** 9 + 7
        a = SortedList()
        ans = 0
        for i in instructions:
            cost = min(a.bisect_left(i), len(a) - a.bisect_right(i))
            ans += cost
            a.add(i)
        return ans % MOD
        '''
        2/2 Binary Indexed Tree.
        Have a BIT that tracks the frequency for each index in instructions.
        Time: O(NlogN) where N is the max of instructions.
        Space: O(N)
        '''
        MOD = 10 ** 9 + 7
        tree = BinaryIndexedTree(max(instructions))
        ans = 0
        for i, a in enumerate(instructions):
            ans += min(tree.get_prefix_sum(a - 1), i - tree.get_prefix_sum(a))
            tree.update(a, 1)
        return ans % MOD

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

    def get_prefix_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= self.low_bit(i)
        return ans