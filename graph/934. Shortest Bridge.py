class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int

        Regular DFS and BFS. When doing DFS, store all positions in the queue for later BFS.
        Either use a set to record the visited positions, or mark the positions as -1.
        """
        rows = len(A)
        cols = len(A[0])
        queue = collections.deque()
        
        def dfs(r, c):
            if not isValid(r, c) or A[r][c] != 1:
                return
            queue.append((r, c))
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
        def findFirstIsland():
            for r in range(rows):
                for c in range(cols):
                    if A[r][c] == 1:
                        dfs(r, c)
                        return
        
        visited = set()
        
        def isValid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in visited
        
        
        findFirstIsland()
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for d in dirs:
                    r2 = r + d[0]
                    c2 = c + d[1]
                    if isValid(r2, c2):
                        if A[r2][c2] == 1:
                            return steps
                        visited.add((r2, c2))
                        queue.append((r2, c2))
            steps += 1