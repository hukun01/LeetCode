# 862. Shortest Subarray with Sum at Least K
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = deque([[0, 0]])
        res, cur = math.inf, 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return -1 if math.isinf(res) else res