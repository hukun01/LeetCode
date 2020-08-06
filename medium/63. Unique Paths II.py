# 63. Unique Paths II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Need to use an external row and colum to cover the cases in which the first row/column has obstacle.
        1/2 2D array
        '''
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        dp[1][0] = 1
        for r in range(R):
            for c in range(C):
                if obstacleGrid[r][c] == 0:
                    dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1]
        return dp[-1][-1]
        '''
        2/2 1D array
        We can optimize this to use a one-dimension array with column size.
        '''
        pathCount = [0] * len(obstacleGrid[0])
        pathCount[0] = 1
        
        for row in obstacleGrid:
            for i, ob in enumerate(row):
                if ob == 1:
                    pathCount[i] = 0
                elif i > 0:
                    pathCount[i] += pathCount[i - 1]
                    
        return pathCount[-1]