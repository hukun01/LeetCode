class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        TODO
        '''
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        rotten = { (r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2 }
        fresh = { (r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1 }
        while fresh:
            if len(rotten) == 0:
                return -1
            newRotten = set()
            for r, c in rotten:
                for dR, dC in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR = r + dR
                    newC = c + dC
                    if (newR, newC) in fresh:
                        newRotten.add((newR, newC))
            fresh -= newRotten
            rotten = newRotten
            minutes += 1
        return minutes