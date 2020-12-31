# 1293. Shortest Path in a Grid with Obstacles Elimination
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        Path finding with a bit tweak.

        We may come to a position multiple times, but we are not sure what
        eliminationCount is each time. This is because there can be a detour
        in the grid with less elimination needed, comparing to a shorter path
        but with more elimination.
        Hence, one key here is to keep track of the (r, c, k) entry instead of
        just (r, c).
        Note, we can NOT early stop! Even if the remaining eliminationCount is
        greater than the total number of cells, we can NOT just return the
        shortest path as 'step + current distance to target', because the
        current step may not be the shortest one, without trying all possible
        elimination.
        However, the idea behind this strategy can still help reduce time
        massively. We just check at the beginning, if k >= shortest path, then
        we don't really need to consider any obstacles.

        Note that BFS would do the same job.

        Time: O(V k + E log(V k)) where V is R*C, as we may visit each cell at
              most k times, each time with a different remaining k.
        Space: O(V k)

        Note that Dijkstra's algorithm is slower than BFS which takes
        O(E + V) time. Overall, Dijkstra's is the same as BFS, if the weights
        among edges are the same. And Dijkstra's can be easily transformed to
        BFS, by changing the priority queue to a deque.
        See this post for details on when Dijkstra's is preferred.
        https://stackoverflow.com/questions/25449781/what-is-difference-between-bfs-and-dijkstras-algorithms-when-looking-for-shorte
        '''
        R, C = len(grid), len(grid[0])
        target = (R - 1, C - 1)
        if sum(target) <= k:
            return sum(target)

        pq = [(0, k, 0, 0)] # (step, remaining_k, r, c)
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while pq:
            step, remaining_k, r, c = heappop(pq)
            if (r, c) == target:
                return step

            if (remaining_k, r, c) in visited:
                continue
            visited.add((remaining_k, r, c))

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if grid[nr][nc] == 0 or remaining_k - 1 >= 0:
                    heappush(pq, (step + 1, remaining_k - (grid[nr][nc] == 1), nr, nc))
        return -1