class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        '''
        Solve 2D problem based on 1D case. In 1D array, we just find the median,
        and sum the distance from each element to the median.
        Note that we find the rowIds and colIds because those ids partially represent the
        distances. And we keep the rowIds and colIds sorted when building the arrays,
        so the median would just be the middle element.
        '''
        rows, cols = len(grid), len(grid[0])
        rowIds = []
        colIds = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowIds.append(r)
        for c in range(cols):
            for r in range(rows):
                if grid[r][c] == 1:
                    colIds.append(c)
        def totalDistance1D(points):
            median = points[len(points) // 2]
            return sum(abs(p - median) for p in points)
        return totalDistance1D(rowIds) + totalDistance1D(colIds)