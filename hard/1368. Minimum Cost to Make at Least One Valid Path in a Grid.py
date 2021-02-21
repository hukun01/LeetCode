# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        1/2 Dijkstra

        Time: O(E + V logV)
        Space: O(E + V)
        '''
        R, C = len(grid), len(grid[0])
        pq = [(0, 0, 0)] # cost, pos (r, c)
        visited = set()
        dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        while pq:
            cost, r, c = heappop(pq)
            if (r, c) == (R - 1, C - 1):
                return cost
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for sign in range(1, 5):
                new_cost = int(sign != grid[r][c])
                dr, dc = dirs[sign]
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                heappush(pq, (new_cost + cost, nr, nc))
        '''
        2/2 BFS.
        Similar to Dijkstra's, but the reason we can use BFS is because we can
        process the weighted edges, because there are only two possible weights
        in the graph, 0 or 1. Hence, the max cost in the queue is at most 1
        more than the min cost in queue. We can make a binary decision based on
        this property.

        The difference between this BFS and usual BFS is that:
        When we find a new node that yields no new cost, we need to add it to
        the left of the queue, because it has less cost than the nodes at tail.

        Time: O(E + V)
        Space: O(E + V)
        '''
        R, C = len(grid), len(grid[0])
        dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        min_cost = [[inf] * C for _ in range(R)]
        q = deque([(0, 0, 0)]) # cost, r, c
        visited = set()
        while q:
            cost, r, c = q.popleft()
            if (r, c) == (R - 1, C - 1):
                return cost
            
            if (r, c) in visited:
                continue

            visited.add((r, c))

            for sign in range(1, 5):
                new_cost = int(sign != grid[r][c])
                dr, dc = dirs[sign]
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if new_cost == 1:
                    q.append((cost + new_cost, nr, nc))
                else:
                    q.appendleft((cost, nr, nc))