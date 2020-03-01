# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        '''
        Pre-calculate the sum of the rectangle whose bottom right is at (r, c),
        then the sum of the square from (top, left) to (bottom, right) can be
        calculated by preSums.
        We then enumerate the length of the edge from (ans + 1), to only look for
        longer length. Total time would be O(RC + min(R, C)), because for each length
        we only use once.
        '''
        rows, cols = len(mat), len(mat[0])
        pre = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                pre[r + 1][c + 1] = pre[r + 1][c] + pre[r][c + 1] - pre[r][c] + mat[r][c]
        
        # (r1, c1) is top left, (r2, c2) is bottom right
        def squareSum(r1, c1, r2, c2):
            return pre[r2][c2] - pre[r1][c2] - pre[r2][c1] + pre[r1][c1]
            
        ans = 0
        for r in range(rows + 1):
            for c in range(cols + 1):
                length = ans + 1
                while r + length <= rows and c + length <= cols and \
                        squareSum(r, c, r + length, c + length) <= threshold:
                    ans = length
                    length += 1
        return ans