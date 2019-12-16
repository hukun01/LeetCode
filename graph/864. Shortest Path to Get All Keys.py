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
        def addKey(keychain, k):
            keychain |= (1 << (ord(k) - ord('a')))
            return keychain
        
        def checkLock(keychain, lock):
            return keychain & (1 << (ord(lock.lower()) - ord('a')))
        
        q = collections.deque()
        targetKey = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    q.append((r, c, 0))
                if grid[r][c].islower():
                    targetKey = addKey(targetKey, grid[r][c])
        def getNextSteps(r, c):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR = dr + r
                newC = dc + c
                if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                    continue
                char = grid[newR][newC]
                if char == '#':
                    continue
                if not char.isupper() or checkLock(key, char):
                    yield (newR, newC)
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
                for newR, newC in getNextSteps(r, c):
                    char = grid[newR][newC]
                    if char.islower():
                        newKey = addKey(key, char)
                        q.append((newR, newC, newKey))
                    else:
                        q.append((newR, newC, key))
            steps += 1
            
        return -1