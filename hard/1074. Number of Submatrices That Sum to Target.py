# 1074. Number of Submatrices That Sum to Target
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        '''
        2D prefix sum + 560. Subarray Sum Equals K

        Compute the 2d prefix sum so we can get the area of a submatrix in O(1)
        time. Then we fix every possible two rows as if it's a single row, and
        do 2-sum like iteration (see #560) and find the count of target area.

        Time: O(RC^2)
        Space: O(RC)
        '''
        R, C = len(matrix), len(matrix[0])
        prefixs = [[0] * (C + 1) for _ in range(R + 1)]
        ans = 0
        for r in range(R):
            for c in range(C):
                prefixs[r+1][c+1] = matrix[r][c] + prefixs[r+1][c] + prefixs[r][c+1] - prefixs[r][c]

        for r0 in range(R):
            for r1 in range(r0+1, R+1):
                seen = defaultdict(int, {0:1})
                for c in range(1, C+1):
                    area = prefixs[r1][c] - prefixs[r0][c]
                    ans += seen[area - target]
                    seen[area] += 1

        return ans