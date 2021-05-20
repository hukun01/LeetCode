class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        '''
        DFS with memoization and pruning.
        '''
        M = 10 ** 9 + 7
        @cache
        def dfs(pos, step):
            if step == 0:
                return int(pos == 0)
            if abs(pos) > step:
                return 0
            if not 0 <= pos < arrLen:
                return 0

            a1 = dfs(pos - 1, step - 1)
            a2 = dfs(pos + 1, step - 1)
            a3 = dfs(pos, step - 1)
            return (a1 + a2 + a3) % M

        return dfs(0, steps)