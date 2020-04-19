# 1349. Maximum Students Taking Exam
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        '''
        1/2 Hungarian algorithm.
        Seats on odd columns and even columns form a bipartite graph.
        Then the maximum independent set on the bipartite graph is the answer.
        '''
        R, C = len(seats), len(seats[0])
        
        matching = [[-1] * C for _ in range(R)]
        
        def dfs(node, seen):
            r, c = node
            for nr, nc in [[r-1,c-1], [r,c-1],[r,c+1],[r-1,c+1],[r+1,c-1],[r+1,c+1]]: # assume a virtual edge connecting students who can spy
                if 0 <= nr < R and 0 <= nc < C and seen[nr][nc] == False and seats[nr][nc] == '.':
                    seen[nr][nc] = True
                    if matching[nr][nc] == -1 or dfs(matching[nr][nc], seen):
                        matching[nr][nc] = (r,c)
                        return True
            return False
        
        def Hungarian():
            res = 0
            for c in range(0,C,2):
                for r in range(R):
                    if seats[r][c] == '.':
                        seen = [[False] * C for _ in range(R)]
                        if dfs((r,c), seen):
                            res += 1
            return res
        
        res = Hungarian()
                
        count = 0
        for r in range(R):
            for c in range(C):
                if seats[r][c] == '.':
                    count += 1
        return count - res
        '''
        2/2 DP.
        dp[r][mask] represents the maximum number for the first r rows with
        students in the r-th row seating as 'mask'.
        The transition function is: dp[i][mask] = max(dp[i - 1][mask']) + number of valid bits(mask)
        
        We need to check two things before using a valid r-th row:
        1. (mask & (mask' >> 1)) == 0, there should be no students in the upper left position for every student.
        2. (mask & (mask' << 1)) == 0, there should be no students in the upper right position for every student.
        '''
        rows, cols = len(seats), len(seats[0])

        validity = [0] * rows
        for r in range(rows):
            cur = 0
            for c in range(cols):
                cur = (cur << 1) | (seats[r][c] == '.')
            validity[r] = cur

        bitCounts = [bin(mask).count("1") for mask in range(1 << cols)]
        
        dp = [[-1] * (1 << cols) for _ in range(rows + 1)]
        dp[0][0] = 0
        for r in range(1, rows + 1):
            valid = validity[r - 1]
            # j is mask, k is mask'
            for j in range(1 << cols):
                # check: 1. mask is valid if it's a subset of 'valid' state
                # check: 2. no students sitting adjacent
                if (j & valid) == j and not (j & (j >> 1)):
                    for k in range(1 << cols):
                        # check: 3. no sutdents in the upper left
                        # check: 4. no students in the upper right
                        # check: 5. last state is good (not -1)
                        if not (j & (k >> 1)) and not (j & (k << 1)) and dp[r - 1][k] != -1:
                            dp[r][j] = max(dp[r][j], dp[r - 1][k] + bitCounts[j])
                            
        return max(dp[-1])