# 315. Count of Smaller Numbers After Self
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        1/2 Using SortedList from sortedcontainers module.
        From right to left, insert each element into the sorted list,
        and the insertion index is the count of the smaller elements.

        Time: O(n log(n))
        Space: O(n)
        '''
        from sortedcontainers import SortedList
        seen = SortedList()
        ans = []
        for a in nums[::-1]:
            ans.append(seen.bisect_left(a))
            seen.add(a)
        return ans[::-1]

        '''
        2/2. Fenwick tree/Binary Indexed Tree.
        A trick here is to convert the original numbers into relative
        ranks, this is to avoid making the BIT's array too big. This technique
        is called Discretization.

        Time: O(n log(n))
        Space: O(n)
        '''
        # BIT works with positive indicies, so start = 1.
        num_to_rank = { v: i for i, v in enumerate(sorted(set(nums)), start = 1) }

        tree = BinaryIndexedTree(len(num_to_rank))
        ans = []
        for a in nums[::-1]:
            rank = num_to_rank[a]
            ans.append(tree.getPrefixSum(rank - 1))
            tree.update(rank, 1)
        return ans[::-1]

class BinaryIndexedTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def low_bit(self, i):
        return i & -i

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