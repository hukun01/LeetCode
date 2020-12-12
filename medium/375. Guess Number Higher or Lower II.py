# 375. Guess Number Higher or Lower II
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            ans = math.inf
            for k in range(i, j + 1):
                ans = min(ans, k + max(dp(i, k-1), dp(k+1, j)))
            return ans
            
        return dp(1, n)