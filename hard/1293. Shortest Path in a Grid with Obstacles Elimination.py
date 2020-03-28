# 1293. Shortest Path in a Grid with Obstacles Elimination
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        Path finding with a bit tweak.

        We may come to a position multiple times, but we are not sure what eliminationCount
        is each time. This is because there can be a detour in the grid with less
        elimination needed, comparing to a shorter path but with more elimination.
        Hence, one key here is to keep track of the (r, c, k) entry instead of just (r, c).
        Also, we can early stop! If the remaining eliminationCount is greater than the
        total number of cells, we can just return the shortest path because we can tear down
        all the obstacles on the path.

        The rest is just like normal path finding. Note that BFS would do the same job.
        '''
        q = [(0, 0, 0, k)] # steps, r, c, k
        R, C = len(grid), len(grid[0])
        seen = set()
        while q:
            steps, r, c, k = heapq.heappop(q)
            if grid[r][c] == 1:
                if k == 0:
                    continue
                k -= 1
            if (r, c) == (R - 1, C - 1):
                return steps
            if R - 1 - r + C - 1 - c <= k:
                return steps + R - 1 - r + C - 1 - c
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if (nr, nc, k) in seen:
                    continue
                seen.add((nr, nc, k))
                heapq.heappush(q, (steps + 1, nr, nc, k))
        return -1