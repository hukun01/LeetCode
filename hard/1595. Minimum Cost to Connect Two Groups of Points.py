# 1595. Minimum Cost to Connect Two Groups of Points
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        '''
        DP.
        TODO.
        '''
        size1, size2 = len(cost), len(cost[0])
        min_arr = [min(x) for x in zip(*cost)]

        @functools.lru_cache(None)
        def dp(i, mask):
            if i == size1:
                return sum(min_arr[j] for j in range(size2) if not (mask & (1 << j)))
            return min(dp(i + 1, mask | (1 << j)) + cost[i][j] for j in range(size2))

        return dp(0, 0)