# 1605. Find Valid Matrix Given Row and Column Sums
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        '''
        Greedy.

        We greedily fill each cell (r, c) with the min(rowSum[r], colSum[c]).
        This means the intersection of rowSum and colSum on this cell can take
        at least the min(rowSum[r], colSum[c]) val.
        After filling the cell with value 'x', we remove 'x' from both the
        rowSum and the colSum.

        Time: O(RC)
        Space: O(RC)
        '''
        R = len(rowSum)
        C = len(colSum)
        ans = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                x = min(rowSum[r], colSum[c])
                rowSum[r] -= x
                colSum[c] -= x
                ans[r][c] = x

        return ans