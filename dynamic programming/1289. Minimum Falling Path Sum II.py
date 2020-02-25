# 1289. Minimum Falling Path Sum II
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        '''
        DP.
        We can sort the last row and get the non-overlapped
        column from the last row, but it's better to just
        pick the smallest two from the last row.
        '''
        rows, cols = len(arr), len(arr[0])
        for r in range(1, rows):
            last = heapq.nsmallest(2, arr[r - 1])
            for c in range(cols):
                if arr[r - 1][c] == last[0]:
                    arr[r][c] += last[1]
                else:
                    arr[r][c] += last[0]
        return min(arr[-1])