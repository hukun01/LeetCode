class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        '''
        BFS.
        BFS from each building, as an early stop strategy, return -1 if that
        BFS can't reach all buildings.
        During BFS, update the distance on each emtpy land and increment the
        hit count, as some lands are not reachable from other buildings.
        Finally, return the smallest distnace on an empty land whose hit
        count == buildingCount.

        One key is to check grid[nr][nc] == 1 and increment local building
        count, but do not allow further processing by not adding it to queue,
        because we cannot pass buildings, but we still need to count it.

        Time: O(N B) where N is the total number of entries in grid, B is the
              number of buildings.
        Space: O(N)
        '''
        buildingCount = sum(val for row in grid for val in row if val == 1)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        R, C = len(grid), len(grid[0])

        distancesAndHits = defaultdict(lambda: [0, 0])
        def bfs(r, c):
            queue = deque([(r, c)])
            visited = [[False for c in range(C)] for r in range(R)]
            distance = 1
            localBuildingCount = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if not 0 <= nr < R or not 0 <= nc < C:
                            continue
                        if visited[nr][nc]:
                            continue
                        visited[nr][nc] = True
                        if grid[nr][nc] == 1:
                            localBuildingCount += 1
                        if grid[nr][nc] > 0:
                            continue
                        distancesAndHits[(nr, nc)][0] += distance
                        distancesAndHits[(nr, nc)][1] += 1
                        queue.append((nr, nc))
                distance += 1
            return localBuildingCount == buildingCount

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    if not bfs(r, c):
                        return -1

        candidates = [distancesAndHit[0] for distancesAndHit in distancesAndHits.values() \
                      if distancesAndHit[1] == buildingCount]
        return -1 if len(candidates) == 0 else min(candidates)