class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        '''
        Use BFS to find the shortest path. Note that we need to store #steps
        as part of the state, because when we hit a lock without the key, we have
        to keep the current steps and position in the queue and come back, because we may
        find the key later.
        Use isupper() to check whether the cell is a lock; Use lower() to convert the lock to its key.
        Use islower() to check whether the cell is a key;
        '''
        def findOffset(char):
            return 1 << (ord(char) - ord('a'))
        rows, cols = len(grid), len(grid[0])
        start = (0, 0)
        finalState = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start = (r, c)
                elif grid[r][c].islower():
                    finalState |= findOffset(grid[r][c])
        q = collections.deque([(0, *start, 0)])
        visited = set()
        while q:
            steps, r, c, state = q.popleft()
            if state == finalState:
                return steps
            for dR, dC in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                newR = r + dR
                newC = c + dC
                if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                    continue
                cell = grid[newR][newC]
                if cell == '#':
                    continue
                # if cell is not lock, or if it's lock and we got the key
                if not cell.isupper() or (state & findOffset(cell.lower())):
                    if cell.islower():
                        newState = state | findOffset(cell)
                    else:
                        newState = state
                    if (newR, newC, newState) not in visited:
                        visited.add((newR, newC, newState))
                        q.append((steps + 1, newR, newC, newState))
        return -1