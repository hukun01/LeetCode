# 943. Find the Shortest Superstring
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def findSuperString(a, b):
            n = min(len(a), len(b))
            res = ''
            maxl = 0 # max shared length
            for i in range(1, n + 1):
                if a.endswith(b[:i]):
                    if maxl < i:
                        res = a + b[i:]
                        maxl = i
            for i in range(1, 1 + n):
                if b.endswith(a[:i]):
                    if maxl < i:
                        res = b + a[i:]
                        maxl = i
            return res, maxl
        p, q = -1, -1
        l = len(A)
        while l != 1:
            # print(A)
            res = ''
            maxl = 0
            for i in range(l):
                for j in range(i + 1, l):
                    res1, cur = findSuperString(A[i], A[j])
                    if maxl < cur:
                        maxl = cur
                        res = res1
                        p = j
                        q = i
            l -= 1
            if len(res) > 0:
                A[p] = res
                A[q] = A[l]
            else:
                A[0] += A[l]
        return A[0]