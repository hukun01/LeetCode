# 499. The Maze III
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        '''
        Dijkstra with Priority Queue.

        The key is to ensure the direction is clear.

        Time: O(RC log(RC)), in the worst case we need to traverse the whole
              maze, and each heappop takes log(RC) time.
        Space: O(RC) for visited.

        Similar to 505. The Maze II
        '''
        visited = set() # pos
        dirs = [('l', 0, -1), ('u', -1, 0), ('d', 1, 0), ('r', 0, 1)]
        pq = [(0, "", tuple(ball))] # steps, path, pos
        R, C = len(maze), len(maze[0])
        hole = tuple(hole)
        while pq:
            steps, path, pos = heappop(pq)
            if pos == hole:
                return path
            if pos in visited:
                continue
            visited.add(pos)
            r, c = pos
            for d, dr, dc in dirs:
                nr = r
                nc = c
                while 0 <= nr + dr < R and 0 <= nc + dc < C and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    if (nr, nc) == hole:
                        break
                if (nr, nc) == (r, c):
                    continue
                heappush(pq, (steps + abs(r - nr) + abs(c - nc), path + d, (nr, nc)))
        return "impossible"