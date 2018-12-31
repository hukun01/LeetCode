class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        pathCount = [0 for _ in obstacleGrid[0]]
        pathCount[0] = 1
        
        for row in obstacleGrid:
            for i, ob in enumerate(row):
                if ob == 1:
                    pathCount[i] = 0
                elif i > 0:
                    pathCount[i] += pathCount[i - 1]
                    
        return pathCount[-1]