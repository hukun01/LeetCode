# 1000. Minimum Cost to Merge Stones
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if (len(stones) - 1) % (K - 1):
            return -1
        preSums = [0] + list(itertools.accumulate(stones))

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + preSums[j + 1] - preSums[i]
            ans = math.inf
            for mid in range(i, j, K - 1):
                ans = min(ans, dp(i, mid, 1) + dp(mid + 1, j, m - 1))
            return ans
        ans = dp(0, len(stones) - 1, 1)
        return ans if ans < inf else -1