class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        '''
        BFS.
        Use BFS to find the shortest path. Note that we need to store keys
        as part of the state, because when we may use a path to grab a key and
        come back later with another key. E.g., in grid [bCa.@AcB], we go left
        to grab 'a', and go right to grab 'c', then go left again to grab 'b'.

        Use isupper() to check whether the cell is a lock;
        Use lower() to convert the lock to its key.
        Use islower() to check whether the cell is a key;
        '''
        def addKey(keychain, k):
            keychain |= (1 << (ord(k) - ord('a')))
            return keychain

        def canUnlock(keychain, lock):
            return keychain & (1 << (ord(lock.lower()) - ord('a')))

        q = deque()
        targetKey = 0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '@':
                    q.append((r, c, 0))
                if grid[r][c].islower():
                    targetKey = addKey(targetKey, grid[r][c])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def getNextSteps(r, c):
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                char = grid[nr][nc]
                if char == '#':
                    continue
                if not char.isupper() or canUnlock(key, char):
                    yield (nr, nc)

        steps = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                r, c, key = q.popleft()
                if key == targetKey:
                    return steps
                if (r, c, key) in visited:
                    continue
                visited.add((r, c, key))
                for nr, nc in getNextSteps(r, c):
                    char = grid[nr][nc]
                    if char.islower():
                        newKey = addKey(key, char)
                        q.append((nr, nc, newKey))
                    else:
                        q.append((nr, nc, key))
            steps += 1

        return -1