# 417. Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        DFS.
        Traverse the graph, two keys:
        1. Find the higher-or-equal reachable points from coast, instead of
           lower-or-equal points, because we are reversely traversing from
           the destination (the coast) back to ANY starting points.
        2. Track the two sets of reachable points from pacific coast and
           atlantic coast, respectively, and their intersection is the answer.

        Time: O(R*C) where R is row count, C is col count.
        Space: O(R*C)

        BFS works the same way.
        '''
        if not matrix or not matrix[0]:
            return []

        R, C = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def find(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if matrix[nr][nc] >= matrix[r][c]:
                    find(nr, nc, visited)

        from_pacific = set()
        from_atlantic = set()

        for r in range(R):
            find(r, 0, from_pacific)
            find(r, C-1, from_atlantic)

        for c in range(C):
            find(0, c, from_pacific)
            find(R-1, c, from_atlantic)

        return sorted(from_pacific.intersection(from_atlantic))