# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        1/2 Dijkstra
        Shortest path in graph.
        Need to handle circle in the grid with a visited set.
        To prune the search paths, we can use heap to track the existing costs
        and only add the exploring nodes when the new cost is smaller.
        '''
        R, C = len(grid), len(grid[0])
        nodes = [(0, (0, 0))]
        end = (R - 1, C - 1)
        visited = set()
        dirs = { 1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0) }
        while nodes:
            cur_cost, cur_node = heappop(nodes)
            if cur_node == end:
                return cur_cost
            r, c = cur_node
            if (r, c) in visited:
                continue
            visited.add(cur_node)
            d = grid[r][c]
            for nd in range(1, 5):
                dr, dc = dirs[nd]
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if d != nd:
                    heappush(nodes, (cur_cost + 1, (nr, nc)))
                else:
                    heappush(nodes, (cur_cost, (nr, nc)))
        '''
        2/2 DFS and BFS.
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