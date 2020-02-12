# 1267. Count Servers that Communicate
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        '''
        Count the # of servers in each row, and col.
        At each cell:
        1. If it's a server;
        2. And if it's row's total + col's total servers > 2,
           note that the server itself was counted as 2, so we need
           to find more than 2 total servers from row and col.
        3. Then this server talk to others, increment the count.
        '''
        g = grid
        rowSums = list(map(sum, g))
        colSums = list(map(sum, zip(*g)))
        count = 0
        for r in range(len(g)):
            for c in range(len(g[0])):
                if g[r][c] == 1 and rowSums[r] + colSums[c] > 2:
                    count += 1
        return count