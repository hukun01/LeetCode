class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        1. Start from the O on the edges, and fill them with Y;
        2. Fill every other O to X
        3. Flip back the Y to O.

        In step1, we need to fill the point upfront to avoid enqueuing them multiple times,
        which makes the space complexity bad. This is a common issue in graph traverse problems.
        '''
        # fill from edges
        def fillFromEdge(r, c):
            board[r][c] = 'Y'
            q = deque([(r, c)])
            while q:
                r0, c0 = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r1, c1 = r0 + dr, c0 + dc
                    if 0 <= r1 < m and 0 <= c1 < n and board[r1][c1] == 'O':
                        q.append((r1, c1))
                        board[r1][c1] = 'Y'

        m, n = len(board), len(board[0])
        for r in range(m):
            for c in (0, n - 1):
                if board[r][c] == 'O':
                    fillFromEdge(r, c)
        
        for c in range(1, n - 1):
            for r in (0, m - 1):
                if board[r][c] == 'O':
                    fillFromEdge(r, c)
        
        # fill every other O to X
        # and flip back the Y to O.
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'Y':
                    board[r][c] = 'O'
