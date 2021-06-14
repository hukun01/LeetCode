# 1900. The Earliest and Latest Rounds Where Players Compete
class Solution:
    def earliestAndLatest(self, n: int, F: int, S: int) -> List[int]:
        @cache
        def dp(l, r, m):
            if l > r:
                return dp(r, l, m)

            if l == r:
                return (1, 1)

            nxt_m = (m + 1) // 2
            ans = [n, 0]
            for i in range(1, l + 1):
                l_win, l_lose = i - 1, l - i
                for j in range(max(r - (m//2) - 1, 0) + l_lose + 1, min(r - 1 - l_win, nxt_m - i) + 1):
                    earliest, latest = dp(i, j, nxt_m)
                    ans = min(ans[0], earliest + 1), max(ans[1], latest + 1)
            return ans

        return dp(F, n - S + 1, n)