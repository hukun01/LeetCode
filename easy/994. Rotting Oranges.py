class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        A BFS problem.

        Keep a fresh set and a rotten set.

        Keep doing below while fresh is not empty:
        If rotten is empty, we can't keep rotting, return -1;

        Go through all the rotten positions, and check their neighbors, if
        a neighbor is in fresh, we can add it to the new_rotten, and remove it from fresh.

        After above, we can replace the rotten with new_rotten.
        '''
        R, C = len(grid), len(grid[0])
        minutes = 0
        rotten = { (r, c) for r in range(R) for c in range(C) if grid[r][c] == 2 }
        fresh = { (r, c) for r in range(R) for c in range(C) if grid[r][c] == 1 }
        while fresh and rotten:
            new_rotten = set()
            for r, c in rotten:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (pos := (nr, nc)) in fresh:
                        new_rotten.add(pos)
                        fresh.remove(pos)
            rotten = new_rotten
            minutes += 1
        return -1 if fresh else minutes