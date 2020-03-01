# 1293. Shortest Path in a Grid with Obstacles Elimination
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        Use BFS, but we also need to keep track of the remaining eliminationCount
        as part of the step.
        Also, since we may come to a position multiple times, we only keep the
        one with the most eliminationCount. In the visited dict, the last
        eliminationCount for a position should be the biggest one.
        '''
        q = [(0, 0, 0, k)] # steps, r, c, K
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for steps, r, c, remainingK in q:
            #steps, r, c, remainingK = q.popleft()
            if r == rows - 1 and c == cols - 1:
                return steps
            if remainingK >= rows - 1 - r + cols - 1 - c - 1:
                return steps + rows - 1 - r + cols - 1 - c
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR = dr + r
                newC = dc + c
                if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                    continue
                if (remainingK, newR, newC) in visited:
                    continue
                visited.add((remainingK, newR, newC))
                if grid[newR][newC] == 1:
                    if remainingK == 0:
                        continue
                    q.append((steps + 1, newR, newC, remainingK - 1))
                else:
                    q.append((steps + 1, newR, newC, remainingK))
        return -1