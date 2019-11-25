class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        '''
        Use a dp(wIdx, takenBikeBits) to represent the assignment up to wIdx and taken bikes represented by bits.
        For each wIdx, iterate through all available bikes.
        '''
        distance = lambda wIdx, bIdx: abs(workers[wIdx][0] - bikes[bIdx][0]) + abs(workers[wIdx][1] - bikes[bIdx][1])
        
        dp = [[0] * (1 << len(bikes)) for _ in range(len(workers))]
        def solve(wIdx, takenBits):
            if wIdx == len(workers):
                return 0
            if dp[wIdx][takenBits] != 0:
                return dp[wIdx][takenBits]
            best = float('inf')
            for bIdx in range(len(bikes)):
                if takenBits & (1 << bIdx) != 0:
                    continue
                best = min(best, distance(wIdx, bIdx) + solve(wIdx + 1, takenBits | (1 << bIdx)))
            dp[wIdx][takenBits] = best
            return best
        return solve(0, 0)