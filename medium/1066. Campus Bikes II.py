class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        '''
        Use a dp(wIdx, takenBikeBits) to represent the assignment up to wIdx and taken bikes represented by bits.
        For each wIdx, iterate through all available bikes.
        '''
        dist = lambda w, b: abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
        cache = {}
        def dfs(wIdx, usedBikes):
            if wIdx == len(workers):
                return 0
            if (wIdx, usedBikes) in cache:
                return cache[(wIdx, usedBikes)]
            d = float('inf')
            for bIdx in range(len(bikes)):
                if usedBikes & (1 << bIdx) != 0:
                    continue
                d = min(d, dist(wIdx, bIdx) + dfs(wIdx + 1, usedBikes | (1 << bIdx)))
            cache[(wIdx, usedBikes)] = d
            return d
        
        return dfs(0, 0)