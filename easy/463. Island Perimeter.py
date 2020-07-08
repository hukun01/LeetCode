# 463. Island Perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        No need to BFS, we just visit each cell, if a cell is land,
        add 4, counting all its boundaries. At the same time, check
        its upper and left cells, if neighbor cell is also land, 
        the number of boundaries is subtracted by 2.
        '''
        R, C = len(grid), len(grid[0])
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans += 4
                    if i > 0 and grid[i-1][j] == 1:
                        ans -=2
                    if j > 0 and grid[i][j-1] == 1:
                        ans -=2
        return ans