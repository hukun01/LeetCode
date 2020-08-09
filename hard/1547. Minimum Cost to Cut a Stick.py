# 1547. Minimum Cost to Cut a Stick
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        '''
        Memoized DFS. A better one is bottom up DP.

        Similar to 312. Burst Balloons.
        '''
        pos = [0] + sorted(cuts) + [n]
        N = len(pos)
        rods = [[pos[i], pos[i + 1]] for i in range(N - 1)]

        @lru_cache(None)
        def dfs(l, r):
            if l >= r:
                return 0
            cost = rods[r][1] - rods[l][0]
            ans = math.inf
            for m in range(l, r):
                ans = min(ans, cost + dfs(l, m) + dfs(m + 1, r))
            return ans
        return dfs(0, len(rods) - 1)