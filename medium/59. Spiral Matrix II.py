# 59. Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        top = left = 0
        bottom = right = n - 1
        i = 0
        end = n ** 2
        while i < end:
            for c in range(left, right):
                ans[top][c] = (i := i + 1)
            for r in range(top, bottom):
                ans[r][right] = (i := i + 1)
            for c in range(right, left, -1):
                ans[bottom][c] = (i := i + 1)
            for r in range(bottom, top, -1):
                ans[r][left] = (i := i + 1)
            if left == right == top == bottom:
                ans[left][top] = (i := i + 1)
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans