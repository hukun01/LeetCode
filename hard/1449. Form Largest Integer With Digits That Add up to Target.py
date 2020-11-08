# 1449. Form Largest Integer With Digits That Add up to Target
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        '''
        1/2 DFS with memoization.

        Let dfs return the answer for given target, then the return value
        is "digit + dfs(remaining_target)".

        Note that the cache entry should be target alone, if the current number
        is included in the cache entry, it would lead to huge time and space complexities.

        Also, we can eliminate smaller digits if there's any large digit with the same cost.
        '''
        bigger_cost_to_idx = {}
        for i, c in enumerate(cost):
            bigger_cost_to_idx[c] = i + 1

        @lru_cache(None)
        def dfs(t):
            if t == 0:
                return -1
            if t < 0:
                return 0
            m = 0
            for c, digit in bigger_cost_to_idx.items():
                x = dfs(t - c)
                if x == 0:
                    continue
                if x != -1:
                    m = max(m, int(str(digit) + str(x)))
                else:
                    m = max(m, digit)
            return m
        x = dfs(target)
        return str(x)
        '''
        2/2 Bottom up DP. Same idea as 1/2 without the trivial optimization with elimination.
        '''
        dp = [0] + [-1] * target
        for t in range(1, target + 1):
            dp[t] = max(
                (dp[t - c] * 10 + i + 1 for i, c in enumerate(cost) if t - c >= 0),
                default=-1)
        return str(max(dp[t], 0))