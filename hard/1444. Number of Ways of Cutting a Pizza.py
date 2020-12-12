# 1444. Number of Ways of Cutting a Pizza
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        '''
        DFS with memoization.
        Build the post-sums matrix to quickly tell whether a submatrix has any apples.
        Then given the top left and bottom right points, we can tell whether it's valid in O(1) time.
        '''
        R, C = len(pizza), len(pizza[0])
        
        # Number of apples from top left (r, c) to the bottom right.
        apples = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                apples[r][c] = apples[r+1][c] + apples[r][c+1] - apples[r+1][c+1]
                apples[r][c] += pizza[r][c] == 'A'
        
        def isValid(r1, c1, r2=R, c2=C):
            return apples[r1][c1] - apples[r2][c1] - apples[r1][c2] + apples[r2][c2] > 0

        MOD = 10 ** 9 + 7

        # r,c is the top left point in the matrix
        @lru_cache(None)
        def dfs(r, c, cuts):
            if cuts == 0:
                if isValid(r, c):
                    return 1
                return 0
            ans = 0
            for r1 in range(r, R-1):
                if isValid(r, c, r1 + 1, C):
                    ans += dfs(r1 + 1, c, cuts - 1)
            for c1 in range(c, C-1):
                if isValid(r, c, R, c1 + 1):
                    ans += dfs(r, c1 + 1, cuts - 1)
            return ans % MOD
            
        return dfs(0, 0, k - 1)