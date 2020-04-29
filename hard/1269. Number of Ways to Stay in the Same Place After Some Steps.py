class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        '''
        DFS with memoization and pruning.
        '''
        @functools.lru_cache(None)
        def dfs(pos, stepsLeft):
            if pos < 0 or pos == arrLen:
                return 0
            if stepsLeft == 0:
                return pos == 0
            if pos > stepsLeft:
                return 0
            a1 = dfs(pos - 1, stepsLeft - 1)
            a2 = dfs(pos + 1, stepsLeft - 1)
            a3 = dfs(pos, stepsLeft - 1)
            return (a1 + a2 + a3) % (10 ** 9 + 7)
        return dfs(0, steps)