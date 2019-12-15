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
        q = collections.deque([(0, 0, k)]) # (r, c, eliminationCount)
        rows, cols = len(grid), len(grid[0])
        visited = collections.defaultdict(list)
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c, e = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return steps
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR = dr + r
                    newC = dc + c
                    if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                        continue
                    newE = e - grid[newR][newC]
                    if newE < 0:
                        continue
                    # The second condition is to only keep the best status, we want more
                    # elimination count at this position.
                    if (newR, newC) not in visited or newE > visited[(newR, newC)][-1][0]:
                        visited[(newR, newC)].append((newE, steps))
                        q.append((newR, newC, newE))
            steps += 1
        return -1