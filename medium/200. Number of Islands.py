# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Union Find.
        This can be solved by DFS/BFS as well, but UF is more natural, and
        UF can solve follow-ups like how to merge/break islands, or count new
        ones if we can make lands or fill the sea.
        With UF, one thing to notice is that we need to connect the left cell
        to the current cell first (current cell is parent), then connect current
        cell to its top cell (top cell is parent). This is to ensure the cells
        are unioned correctly.
        '''
        if not grid or not grid[0]:
            return 0
        uf = {}
        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        R = len(grid)
        C = len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '0':
                    continue
                curr = find((r, c))
                if c > 0 and grid[r][c-1] == '1':
                    left = find((r, c-1))
                    uf[left] = curr
                if r > 0 and grid[r-1][c] == '1':
                    top = find((r-1, c))
                    uf[curr] = top
        return len({find(x) for x in uf})