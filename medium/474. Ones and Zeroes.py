# 474. Ones and Zeroes
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        1/2 DP.
        Let f[i][j][k] be the answer for the first i strs, with j 0s, and k 1s.
        f[i][j][k] = max(item1, item2)
        item1: f[i-1][j][k], we don't take the i-th str
        item2: f[i-1][j - zeros][k - ones] + 1, we take it, if we have enough 0s and 1s.

        We can optmize the space based on the fact that f[i] only depends on f[i-1].
        After that we can also improve runtime performance by iterating j in range(m, zeros-1, -1),
        similar for k.
        '''
        f = [[[0] * (n + 1) for j in range(m + 1)] for i in range(len(strs) + 1)]
        for i, s in enumerate(strs, 1):
            zeros = s.count('0')
            ones = len(s) - zeros
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zeros and k >= ones:
                        f[i][j][k] = max(f[i-1][j][k], f[i-1][j - zeros][k - ones] + 1)
                    else:
                        f[i][j][k] = f[i-1][j][k]

        return f[len(strs)][m][n]
        '''
        2/2 Memoized DFS.
        Easier and more straightfoward, but not as good as bottom up DP in so many aspects.
        '''
        counts = []
        for s in strs:
            c = Counter(s)
            counts.append((c['0'], c['1']))

        @lru_cache(None)
        def dfs(idx, m_remain, n_remain):
            if idx == len(counts):
                return 0
            c0, c1 = counts[idx]
            ans = 0
            if m_remain >= c0 and n_remain >= c1:
                ans = 1 + dfs(idx + 1, m_remain - c0, n_remain - c1)
            ans = max(ans, dfs(idx + 1, m_remain, n_remain))
            return ans

        return dfs(0, m, n)