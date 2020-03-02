class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        Regular DFS and BFS. Do DFS to find the first island, and store all positions in the queue for later BFS.
        Either use a set to record the visited positions, or mark the positions as -1.
        """
        q = collections.deque()
        rows, cols = len(A), len(A[0])
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            if not valid(r, c) or A[r][c] != 1:
                return
            A[r][c] = 2
            q.append((r, c))
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
        def mark():
            for r in range(rows):
                for c in range(cols):
                    if A[r][c] == 1:
                        dfs(r, c)
                        return
        mark()
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = dr + r, dc + c
                    if not valid(nr, nc) or A[nr][nc] == 2:
                        continue
                    if A[nr][nc] == 1:
                        return steps
                    A[nr][nc] = 2
                    q.append((nr, nc))
            steps += 1