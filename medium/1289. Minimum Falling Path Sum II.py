# 1289. Minimum Falling Path Sum II
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        '''
        DP.
        We can pick the smallest two from the previous row.
        Then update the current row with either of the two smallest.
        '''
        n = len(arr)
        prev = arr[0][:]
        for r in range(1, n):
            smallest = nsmallest(2, prev)
            cur = arr[r][:]
            for c in range(n):
                if prev[c] == smallest[0]:
                    cur[c] += smallest[1]
                else:
                    cur[c] += smallest[0]
            prev = cur
        return min(prev)