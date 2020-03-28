class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        '''
        Use a dp(wIdx, takenBikeBits) to represent the assignment up to wIdx and taken bikes represented by bits.
        For each wIdx, iterate through all available bikes.
        '''
        dist = lambda w, b: abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
        
        @functools.lru_cache(None)
        def dfs(w, usedBikes):
            if w == len(workers):
                return 0
            ans = math.inf
            for b in range(len(bikes)):
                if usedBikes & (1 << b) == 0:
                    ans = min(ans, dist(w, b) + dfs(w + 1, usedBikes | (1 << b)))
            return ans
        return dfs(0, 0)