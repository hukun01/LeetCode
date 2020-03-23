# 1391. gCheck if There is a Valid Path in a Grid
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        '''
        1/2 Extend the grid to make it path clearer, and BFS/DFS.
        The 6 street shapes essentially tell what directions they connect to,
        So we make each cell a 3x3 bigger cell, as below.
        Then we use 2-end BFS to reduce keeping track of too many entries.
        '''
        g = grid
        if not g or not g[0]:
            return False
        gR, gC = len(g), len(g[0])
        mR, mC = 3 * gR, 3 * gC
        m = [[0] * mC for _ in range(mR)]
        for r in range(gR):
            for c in range(gC):
                r0 = r * 3 + 1
                c0 = c * 3 + 1
                if g[r][c] == 1:
                    m[r0][c0-1] = m[r0][c0] = m[r0][c0+1] = 1
                if g[r][c] == 2:
                    m[r0-1][c0] = m[r0][c0] = m[r0+1][c0] = 1
                if g[r][c] == 3:
                    m[r0][c0] = m[r0][c0 - 1] = m[r0 + 1][c0] = 1
                if g[r][c] == 4:
                    m[r0][c0] = m[r0][c0 + 1] = m[r0 + 1][c0] = 1
                if g[r][c] == 5:
                    m[r0][c0] = m[r0][c0 - 1] = m[r0 - 1][c0] = 1
                if g[r][c] == 6:
                    m[r0][c0] = m[r0][c0 + 1] = m[r0 - 1][c0] = 1
        start = {(1, 1)}
        end = {(mR - 2, mC - 2)}
        seen = [[False] * mC for _ in range(mR)]
        while start and end:
            if len(start) < len(end):
                start, end = end, start
            nextLevel = set()
            for r, c in start:
                if (r, c) in end:
                    return True
                if seen[r][c]:
                    continue
                seen[r][c] = True
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = dr + r, dc + c
                    if not 0 <= nr < mR or not 0 <= nc < mC:
                        continue
                    if m[nr][nc] == 0:
                        continue
                    nextLevel.add((nr, nc))
            start = nextLevel
        return False
        '''
        2/2 Without extending the grid, we do direct BFS.
        We check adjacent cells and compare their directions with
        current cell and its direction. If both direction match, two cells
        can connect.
        '''
        g = grid
        if not g or not g[0]:
            return False
        gR, gC = len(g), len(g[0])
        dirs = [
            [[0, 0] , [0, 0]], # 0th is a placeholder for index shift
            [[0, -1], [0, 1]],
            [[-1, 0], [1, 0]],
            [[0, -1], [1, 0]],
            [[0, 1], [1, 0]],
            [[0, -1], [-1, 0]],
            [[0, 1], [-1, 0]]
        ]
        q = [(0, 0)]
        seen = [[False] * gC for _ in range(gR)]
        for r, c in q:
            if seen[r][c]:
                continue
            seen[r][c] = True
            for dr, dc in dirs[g[r][c]]:
                nr, nc = dr + r, dc + c
                if not 0 <= nr < gR or not 0 <= nc < gC:
                    continue
                for backDr, backDc in dirs[g[nr][nc]]:
                    if nr + backDr == r and nc + backDc == c:
                        q.append((nr, nc))
                        break
        return seen[gR - 1][gC - 1]