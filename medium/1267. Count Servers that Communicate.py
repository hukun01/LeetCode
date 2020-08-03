# 1267. Count Servers that Communicate
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        '''
        Count the # of servers in each row, and col.
        At each cell:
        1. If it's a server;
        2. And if its row's total + col's total servers > 2,
           because each server itself was counted as 2, we need
           to find more than 2 total servers from row and col.
        3. Then this server talk to others, increment the count.

        Note zip(*matrix) can traverse the matrix column by column.
        '''
        g = grid
        row_sums = list(sum(row) for row in g)
        col_sums = list(sum(col) for col in zip(*g))
        count = 0
        for r in range(len(g)):
            for c in range(len(g[0])):
                if g[r][c] == 1 and row_sums[r] + col_sums[c] > 2:
                    count += 1
        return count