class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        State transition: path[r][c] = min(path[r - 1][c], path[r][c - 1]) + grid[r][c],
        we just need to initialize the first row and column.
        This 2D space can be reduced to 1D because we only used the current row and the last row.
        """
        path = [0 for g in grid[0]]
        path[0] = grid[0][0]
        for c in range(1, len(grid[0])):
            path[c] = path[c - 1] + grid[0][c]
            
        for row in grid[1:]:
            for c, g in enumerate(row):
                if c == 0:
                    path[c] += g
                else:
                    path[c] = min(path[c], path[c - 1]) + g
        return path[-1]