class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        '''
        DFS with memoization and pruning.
        '''
        cache = {}
        def dfs(pos, steps):
            if (pos, steps) in cache:
                return cache[(pos, steps)]
            if steps == 0:
                if pos == 0:
                    return 1
                return 0
            if pos >= arrLen or \ # We are at the rightmost end;
                pos > steps or \  # Don't have enough steps to go back from right to origin;
                pos < 0:          # Out of allowable range.
                return 0
            result = 0
            result += dfs(pos, steps - 1)
            result += dfs(pos + 1, steps - 1)
            result += dfs(pos - 1, steps - 1)
            result %= 10**9+7
            cache[(pos, steps)] = result
            return result
        return dfs(0, steps)