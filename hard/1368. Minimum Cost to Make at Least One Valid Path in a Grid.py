# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        Shortest path in graph.
        Need to handle circle in the grid with a visited set.
        To prune the search paths, we can use track the existing costs
        and only add the exploring nodes when the new cost is smaller.
        '''
        rows, cols = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        while heap:
            cost, r, c = heapq.heappop(heap)
            if visited[r][c]:
                continue
            visited[r][c] = True
            if (r, c) == (rows-1, cols-1):
                return cost
            for i, (dr, dc) in enumerate(dirs):
                nr, nc = dr + r, dc + c
                newCost = cost + (i != grid[r][c]-1)
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(heap, (newCost, nr, nc))