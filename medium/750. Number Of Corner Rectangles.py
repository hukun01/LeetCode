# 750. Number Of Corner Rectangles
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        '''
        1/2 DP.
        At the current position (r1, c1), check the next columns, and record
        the column pair (c1, c2) that are both 1.
        In the next rows, whenever we see (c1, c2) again, we know there's a
        rectangle. To generalize, at a row, if it has (c1, c2), then the
        frequencies of previous (c1, c2) is the number of new rectangles.

        Time: O(R C^2)
        Space: O(C^2)
        '''
        count = Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1 == 0:
                    continue
                for c2 in range(c1 + 1, len(row)):
                    if row[c2] == 0:
                        continue
                    ans += count[c1, c2]
                    count[c1, c2] += 1
        return ans
        '''
        2/2 DP optimized.
        With the same time complexity, we can enumerate each (c1, c2) in O(C^2)
        time, and for each (c1, c2), we scan the whole rows, and do the same
        counting as 1/2.
        Note that due to LeetCode's poor test cases, O(R C^2) would TLE in
        Python, but not in some other languages. Here we do O(C R^2) that can
        pass, but the logic is identical.

        Time: O(R^2 C)
        Space: O(1)
        '''
        R, C = len(grid), len(grid[0])
        ans = 0
        for r1 in range(R):
            for r2 in range(r1 + 1, R):
                count = 0
                for c in range(C):
                    if grid[r1][c] and grid[r2][c]:
                        ans += count
                        count += 1
        return ans