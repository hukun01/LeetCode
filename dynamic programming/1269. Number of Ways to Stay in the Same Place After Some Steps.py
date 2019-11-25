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
            # 1. We are at the rightmost end;
            # 2. Don't have enough steps to go back from right to origin;
            # 3. Out of allowable range.
            if pos >= arrLen or pos > steps or pos < 0:
                return 0
            result = 0
            result += dfs(pos, steps - 1)
            result += dfs(pos + 1, steps - 1)
            result += dfs(pos - 1, steps - 1)
            cache[(pos, steps)] = result
            return result
        return dfs(0, steps) % (10**9 + 7)