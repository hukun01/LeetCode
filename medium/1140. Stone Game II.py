# 1140. Stone Game II
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        '''
        DFS with memoization.
        
        DFS returns the max gain that the current player can get by starting from i,
        so it's the max(total number of stones from i to end (denoted by suffixSums[i])
        minus the max stone the other player can get) with all possible steps the current
        player can make.
        '''
        suffixSums = list(piles)
        for i in range(len(piles) - 2, -1, -1):
            suffixSums[i] += suffixSums[i + 1]

        @lru_cache(None)
        def dfs(i, m):
            if i + 2 * m >= len(piles):
                return suffixSums[i]
            ''' 1/2 Find an x that minimizes the other player's gain.
            minStones = math.inf
            for x in range(1, 2 * m + 1):
                minStones = min(minStones, dfs(i + x, max(m, x)))
            return suffixSums[i] - minStones
            '''
            # 2/2 Find an x that maximizes the current player's gain.
            maxStones = 0
            for x in range(1, 2 * m + 1):
                maxStones = max(maxStones, suffixSums[i] - dfs(i + x, max(m, x)))
            return maxStones
            
        return dfs(0, 1)