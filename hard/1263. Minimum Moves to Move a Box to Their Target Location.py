# 1263. Minimum Moves to Move a Box to Their Target Location
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        '''
        Dijkstra.
        can_reach() can be improved with Tarjan
        '''
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        b_pos = s_pos = t_pos = None
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'B':
                    b_pos = (r, c)
                if grid[r][c] == 'S':
                    s_pos = (r, c)
                if grid[r][c] == 'T':
                    t_pos = (r, c)
        def is_empty(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] != '#'

        def can_reach(r1, c1, r2, c2, br, bc):
            if not is_empty(r2, c2):
                return False
            q = [(r1, c1)]
            used = set()
            for r, c in q:
                if (r, c) in used or (r, c) == (br, bc):
                    continue
                used.add((r, c))
                if (r, c) == (r2, c2):
                    return True
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if is_empty(nr, nc):
                        q.append((nr, nc))
            return False
        visited = set()
        pq = [(0, b_pos, s_pos)]
        while pq:
            steps, b_pos, s_pos = heappop(pq)
            if (b_pos, s_pos) in visited:
                continue
            visited.add((b_pos, s_pos))
            if b_pos == t_pos:
                return steps
            sr, sc = s_pos
            br, bc = b_pos
            for dr, dc in dirs:
                br1, bc1 = br + dr, bc + dc
                br2, bc2 = br - dr, bc - dc
                if is_empty(br2, bc2) and can_reach(sr, sc, br1, bc1, br, bc):
                    heappush(pq, (steps + 1, (br2, bc2), b_pos))
        return -1