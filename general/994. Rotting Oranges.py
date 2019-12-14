class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        A BFS problem.

        Keep a fresh set and a rotten set.
        
        Keep doing below while fresh is not empty:
        If rotten is empty, we can't keep rotting, return -1;

        Go through all the rotten positions, and check their neighbors, if
        a neighbor is in fresh, we can add it to the newRotten, and remove it from fresh.

        After above, we can replace the rotten with newRotten.
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
                        fresh.remove((newR, newC))
            rotten = newRotten
            minutes += 1
        return minutes