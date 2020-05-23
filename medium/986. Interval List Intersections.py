# 986. Interval List Intersections
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = b = 0
        ans = []
        while a < len(A) and b < len(B):
            start = max(A[a][0], B[b][0])
            end = min(A[a][1], B[b][1])
            if start <= end:
                ans.append([start, end])
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        return ans