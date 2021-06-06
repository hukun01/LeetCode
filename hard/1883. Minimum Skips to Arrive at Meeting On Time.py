# 1883. Minimum Skips to Arrive at Meeting On Time
class Solution:
    def minSkips(self, dist: List[int], S: int, hoursBefore: int) -> int:
        '''
        DP.

        Let f[i][k] be the min hour to arrive at dist[i-1] with k skips.
        f[i][k] = min(f[i-1][j-1] + d, (f[i-1][j] + d + S - 1) // S * S)

        The key is that in this transition function we actually use 'hour * S'
        instead of just hour, because the hour can be floating numbers, and has
        accuracy issue.

        Time: O(n^2) where n is len(dist)
        Space: O(n^2), can be reduced to O(n) as f[i] only depends on f[i-1]
        '''
        n = len(dist)
        f = [[inf] * (n + 1) for _ in range(n+1)]
        f[0][0] = 0
        for i, d in enumerate(dist, 1):
            f[i][0] = (f[i-1][0] + d + S - 1) // S * S
            for j in range(1, i + 1):
                f[i][j] = min(f[i-1][j-1] + d, (f[i-1][j] + d + S - 1) // S * S)

        return next((j for j, t in enumerate(f[-1]) if t <= hoursBefore * S), -1)