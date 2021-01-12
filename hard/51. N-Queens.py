# 51. N-Queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        DFS.
        The key is to quickly check whether a queen can sit on a cell.

        Whenever a location (x, y) is occupied, any other locations
        (r, c) where r + c == x + y or r - c == x - y would be invalid.
        This is because if (r, c) satisfies above equations, it will be on
        one of the two diagonal lines: y = x + b, or y = -x + b.
        And if r + c == x + y == b, then they are on the same line.
        Same applies to r - c == x - y == -b.

        Now from all the cols that haven't been used or on the diagonal,
        it's a valid col, append to the path. Each col's index is the row.
        '''
        def dfs(queens, xy_dif, xy_sum):
            r = len(queens)
            if r == n:
                ans.append(queens)
                return
            for c in range(n):
                if (r - c) not in xy_dif and (r + c) not in xy_sum and c not in queens:
                    # Can easily convert below code into backtracking logic
                    dfs(queens + [c], xy_dif | {r - c}, xy_sum | {r + c})  
        ans = []
        dfs([], set(), set())
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]