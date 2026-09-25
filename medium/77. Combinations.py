class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        '''
        Backtracking.
        We add each number in [start, n] to the current path, and enter DFS
        each time.
        In each DFS we do the same - add the starting number to the path.
        When entering DFS, we need to advance the starting point to avoid
        duplicates.
        When the path's length becomes k, we presist the result and return.
        When a DFS ends, we pop out the last element from the path, so we can
        explore the next value.
        '''
        ans = []
        def dfs(path, start):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                dfs(path, i + 1)
                path.pop()
        dfs([], 1)
        return ans
