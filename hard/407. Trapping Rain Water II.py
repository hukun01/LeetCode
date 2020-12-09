# 407. Trapping Rain Water II
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        '''
        Priority queue.
        Similar to 1-d version, we need to find the boundaries of areas.
        The key is to notice that in the 2-d map, when there are multiple
        connected cells, the water can flow out through the lowest one. Hence,
        the lowest boundary determines the volume of water that can be trapped.
        We need to keep track of the current lowest height, starting from the 4
        walls around the map, to ensure we only start from lower positions.
        And record the current max of the seen lowest heights, this is the
        lowest boundary of its area. Then check the current lowest position's
        neighbors, add water if possible, and add neighbors to the boundaries
        priority queue.

        Time: O(RC log(R+C))
        Space: O(RC) for visited
        '''
        R, C = len(heightMap), len(heightMap[0])
        lowest = []
        visited = [[False] * C for _ in range(R)]
        for r in range(R):
            lowest.extend([(heightMap[r][0], r, 0), (heightMap[r][C - 1], r, C - 1)])
            visited[r][0] = visited[r][C - 1] = True
        for c in range(C):
            lowest.extend([(heightMap[0][c], 0, c), (heightMap[R - 1][c], R - 1, c)])
            visited[0][c] = visited[R - 1][c] = True
        heapify(lowest)

        cur_max_height = 0
        ans = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while lowest:
            cur_min, r, c = heappop(lowest)
            cur_max_height = max(cur_max_height, cur_min)
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                ans += max(0, cur_max_height - heightMap[nr][nc])
                heappush(lowest, (heightMap[nr][nc], nr, nc))
        return ans