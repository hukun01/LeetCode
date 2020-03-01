class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Need to use an external row and colum to cover the cases in which the first row/column has obstacle.
        1/2 2D array

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for c in range(cols + 1)] for r in range(rows + 1)]
        dp[1][0] = 1
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    dp[r+1][c+1] = 0
                else:
                    dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1]
        return dp[-1][-1]

        2/2 1D array
        We can optimize this to use a one-dimension array with column size.
        """
        pathCount = [0] * len(obstacleGrid[0])
        pathCount[0] = 1
        
        for row in obstacleGrid:
            for i, ob in enumerate(row):
                if ob == 1:
                    pathCount[i] = 0
                elif i > 0:
                    pathCount[i] += pathCount[i - 1]
                    
        return pathCount[-1]