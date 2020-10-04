# 1605. Find Valid Matrix Given Row and Column Sums
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        '''
        Array.
        North-west corner method.
        We initialize the whole array with 0, then only fill places where
        positive values present.

        A heuristic is that, overall, we want to update minimum number of
        cells, and leave the rest be 0, so we update cells with the maximum
        possible values, and remove the value from rowSum and colSum.

        The maximum possible value at each cell [r,c], it's the minimum
        between (rowSum[r], colSum[c]). Any number greater than this would
        cause the row sum or col sum to be too big.
        If we picked the rowSum[r], next time we use the next row. If we
        picked the colSum[c], next time we use the next col.

        Note that this only works when sum(rowSum) == sum(colSum).
        '''
        R = len(rowSum)
        C = len(colSum)
        r = c = 0
        A = [[0] * C for i in range(R)]
        while r < R and c < C:
            val = min(rowSum[r], colSum[c])
            A[r][c] = val
            rowSum[r] -= val
            colSum[c] -= val
            if rowSum[r] == 0:
                r += 1
            if colSum[c] == 0:
                c += 1
        return A