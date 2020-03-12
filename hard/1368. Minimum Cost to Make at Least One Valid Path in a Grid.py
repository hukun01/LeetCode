# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        1/2 DFS and BFS.
        From each position, start a DFS without changing direction, see
        how far we can go. This will define the minimum cost to reach
        the positions.
        From all the positions we can reach without changing direction,
        try the other 3 directions (with incremented cost) and see how
        far we can go.
        '''
        A = grid
        rows, cols, inf = len(A), len(A[0]), 10**9
        dp = [[inf] * cols for _ in range(rows)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(queue, r, c, currCost):
            if not (0 <= r < rows and 0 <= c < cols and dp[r][c] == inf): return
            dp[r][c] = currCost
            queue.append([r, c])
            dr, dc = dirs[A[r][c] - 1]
            dfs(queue, r + dr, c + dc, currCost)

        queue = []
        cost = 0
        dfs(queue, 0, 0, cost)
        while queue:
            cost += 1
            queue, queue2 = [], queue
            for r, c in queue2:
                for dr, dc in dirs:
                    dfs(queue, r + dr, c + dc, cost)
        return dp[-1][-1]

        '''
        2/2 Dijkstra
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
            for dr, (dr, dc) in enumerate(dirs):
                nr, nc = dr + r, dc + c
                newCost = cost + (dr != grid[r][c]-1)
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(heap, (newCost, nr, nc))