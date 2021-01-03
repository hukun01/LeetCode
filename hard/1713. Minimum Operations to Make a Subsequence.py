# 1713. Minimum Operations to Make a Subsequence
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        '''
        Transform from LCS to LIS and DP.
        It's obvious that this is a LCS problem (longest common subsequence),
        but it would TLE as the time is O(m n) where n is len(target), m is
        len(arr).
        Notice that all elements in target are *distinct*, thus, we can use
        target element's index as its 'value', and find the longest increasing
        subsequence of these 'values' in arr. The mismatched part is where we
        need to insert.

        The key here is to represent the distinct unsorted numbers by their
        indices, which are sorted.

        Time: O(n log (n)) where n is len(target)
        Space: O(n)
        '''
        def LIS(nums):  # standard LIS
            n = len(nums)
            lens = [inf] * (n + 1)
            for a in nums:
                lens[bisect_left(lens, a)] = a
            return bisect_left(lens, inf)

        val2idx = { a: i for i, a in enumerate(target) }
        idxs = [val2idx[a] for a in arr if a in val2idx]
        return len(target) - LIS(idxs)