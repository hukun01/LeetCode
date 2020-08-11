# 1547. Minimum Cost to Cut a Stick
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        '''
        1/2 Memoized DFS.

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
        '''
        2/2 DP.
        Note that we need to handle one base case separately: for sticks
        with length 1, there's nothing to cut, so cost is always 0.
        
        '''
        cuts = sorted(cuts + [0, n])
        N = len(cuts)
        f = [[math.inf] * N for _ in range(N)]
        for left in range(N-1):
            f[left][left + 1] = 0
        for length in range(2, N):
            for left in range(N - length):
                right = left + length
                for i in range(left + 1, right):
                    f[left][right] = min(
                        f[left][right],
                        f[left][i] + f[i][right] + cuts[right] - cuts[left])
        return f[0][N-1]