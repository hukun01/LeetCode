# 526. Beautiful Arrangement
class Solution:
    def countArrangement(self, n: int) -> int:
        '''
        DFS backtracking.
        Try filling each index 'i', and use 'visited' to avoid reusing numbers.
        Filling from the largest to the smallest, is faster, than the opposite,
        because the 1st position can hold any number, but later permutation may
        not be valid, e.g., n = 3, and the current path is [3, 1, ], this path
        will be discarded. If we start from backward, we have [x, x, 3] or
        [x, x, 1], only two branches.
        '''
        visited = set()
        def dfs(i):
            if i == 1:
                return 1
            ans = 0
            for x in range(1, n + 1):
                if x not in visited and (i % x == 0 or x % i == 0):
                    visited.add(x)
                    ans += dfs(i - 1)
                    visited.remove(x)
            return ans
        return dfs(n)