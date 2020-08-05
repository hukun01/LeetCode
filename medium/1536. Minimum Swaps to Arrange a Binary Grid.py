# 1536. Minimum Swaps to Arrange a Binary Grid
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        '''
        Greedy.
        This is about rearranging the rows in the grid, and
        each row's value is the number of consecutive trailing
        zeros.
        At each row, if its value is greater than needed, skip it,
        because we only need smaller values in the next rows. If at
        any row we can't find a large enough value, there's no good
        arrangement at all.
        If its value is smaller than needed, then we need to find a
        greater value in the next rows, by swapping rows one by one.
        Find the closest row with sufficient value, and swap it up
        one by one and increment 'ans' each time.
        '''
        rows = []
        n = len(grid)
        for row in grid:
            count = 0
            for i in range(n-1, -1, -1):
                if row[i] != 0:
                    break
                count += 1
            rows.append(count)
        ans = 0
        for i in range(n):
            need = n - i - 1
            if rows[i] >= need:
                continue
            found = next((j for j in range(i, n) if rows[j] >= need), None)
            if not found:
                return -1
            for x in range(found, i, -1):
                rows[x], rows[x-1] = rows[x-1], rows[x]
                ans += 1
        return ans