# 505. The Maze II
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        Dijkstra with Priority Queue.

        Time: O(RC log(RC)), in the worst case we need to traverse the whole
              maze, and each heappop takes log(RC) time.
        Space: O(RC) for visited.
        '''
        visited = set() # pos
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(0, tuple(start))] # steps, pos
        dest = tuple(destination)
        R, C = len(maze), len(maze[0])
        while pq:
            steps, pos = heappop(pq)
            if pos == dest:
                return steps
            if pos in visited:
                continue
            visited.add(pos)
            r, c = pos
            for dr, dc in dirs:
                nr = r
                nc = c
                while 0 <= nr + dr < R and 0 <= nc + dc < C and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) == (r, c):
                    continue
                heappush(pq, (steps + abs(r - nr) + abs(c - nc), (nr, nc)))
        return -1