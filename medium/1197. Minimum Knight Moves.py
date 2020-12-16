# 1197. Minimum Knight Moves
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        Memoized DFS.
        The key is to recognize that we only need to check one of the 4 
        direction blocks. Hence we only deal with abs(x) and abs(y).

        Another key is to handle the boundary when x + y = 2. In this case,
        it's either (1, 1) or (0, 2) or (2, 0), in chess it takes 2 steps to go
        to (0, 0). For example, (1, 1) -> (2, -1) -> (0, 0). We need to treat
        these specially because they need to go to other blocks that we ignore
        in the first key logic.

        Time: O(max(x, y))
        Space: O(xy)
        '''
        @cache
        def dfs(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            return 1 + min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1)))
        return dfs(abs(x), abs(y))