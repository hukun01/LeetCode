class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        '''
        1/2 Finding the median.

        In 1D array, the median point minimizes the total distance between
        every point to the median point.
        In 2D array, there are 2 moving directions. One is from left/right col
        to middle col; Another is from top/bottom row to middle row.
        Hence, we find the column-wise array, and row-wise array, and feed them
        to the 1D process, and find the total distance.

        We find the row_ids and col_ids of homes, because those ids partially
        represent the distances.

        For example, row0 has 3 homes, row1 has 0 home, row2 has 1 home, then
        the row_ids would be [0,0,0,2], this way we know that we should meet at
        row0, because it has more homes.

        Note that we keep the row_ids and col_ids sorted when building the
        arrays, so the median would just be the middle element.

        Time: O(R C)
        Space: O(R C)
        '''
        R, C = len(grid), len(grid[0])
        row_ids = []
        col_ids = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    row_ids.append(r)
        for c in range(C):
            for r in range(R):
                if grid[r][c] == 1:
                    col_ids.append(c)
        def total_distance_1D(points):
            median = points[len(points) // 2]
            return sum(abs(p - median) for p in points)
        return total_distance_1D(row_ids) + total_distance_1D(col_ids)
        '''
        2/2 A similar, suboptimal, but more straightforward approach.
        This directly implements the idea in 1/2, and use a brute force way
        to find the least moves.

        Time: O(max(R, C) ^ 2)
        Space: O(max(R, C))
        '''
        R, C = len(grid), len(grid[0])
        rows_count = [sum(grid[r]) for r in range(R)]
        cols_count = [sum(grid[r][c] for r in range(R)) for c in range(C)]

        def find_least_moves_1D(arr):
            ans = inf
            n = len(arr)
            for i in range(n):
                cur = sum(arr[j] * abs(i - j) for j in range(n) if i != j)
                ans = min(ans, cur)
            return ans

        return find_least_moves_1D(rows_count) + find_least_moves_1D(cols_count)