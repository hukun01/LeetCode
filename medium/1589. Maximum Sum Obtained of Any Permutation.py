# 1589. Maximum Sum Obtained of Any Permutation
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
        Greedy + difference array.

        The key is to count the total frequencies for each index, from
        requests, without 2d loop. This is similar to 370. Range Addition.

        Time: O(n log(n)) where n is len(nums)
        Space: O(n)
        '''
        MOD = 10 **9 + 7
        n = len(nums)
        diffs = [0] * n
        for s, e in requests:
            diffs[s] += 1
            if e + 1 < n:
                diffs[e + 1] -= 1

        counts = sorted(accumulate(diffs))
        nums.sort()
        ans = 0
        for c, a in zip(counts, nums):
            ans = (ans + c * a) % MOD
        return ans