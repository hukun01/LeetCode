class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Need to use an external row and colum to cover the cases in which the first row/column has obstacle.
        Then we can optimize this to use a one-dimension array with column size.
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