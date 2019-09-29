class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # BFS from each building, as an early stop strategy, return -1 if 
        # that BFS can't reach all buildings.
        # During BFS, update the distance on each emtpy land and increment the
        # hit count, as some lands are not reachable from other buildings.
        # Finally, return the smallest distnace on an empty land whose hit count == buildingCount.
        buildingCount = sum(val for row in grid for val in row if val == 1)
        compass = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        
        distancesAndHits = [[[0, 0] for c in range(cols)] for r in range(rows)]
        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visited = [[False for c in range(cols)] for r in range(rows)]
            distance = 1
            localBuildingCount = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for d in compass:
                        newR = r + d[0]
                        newC = c + d[1]
                        if 0 <= newR < rows and 0 <= newC < cols:
                            if visited[newR][newC]:
                                continue
                            visited[newR][newC] = True
                            if grid[newR][newC] == 1:
                                localBuildingCount += 1
                            if grid[newR][newC] > 0:
                                continue
                            distancesAndHits[newR][newC][0] += distance
                            distancesAndHits[newR][newC][1] += 1
                            queue.append((newR, newC))
                distance += 1
            return localBuildingCount == buildingCount

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if not bfs(r, c):
                        return -1
        
        candidates = [distancesAndHits[r][c][0] for r in range(rows) \
                      for c in range(cols) if distancesAndHits[r][c][1] == buildingCount]
        return -1 if len(candidates) == 0 else min(candidates)