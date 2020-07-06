# 718. Maximum Length of Repeated Subarray
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        '''
        1/2 DP
        Similar to 1143. Longest Common Subsequence
        Let f[a][b] be the answer for A[:a] and B[:b]
        f[a][b] = f[a-1][b-1] + 1 if A[a-1] == B[b-1] else 0
        answer is max(f).
        '''
        f = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        ans = 0
        for a in range(len(A) + 1):
            for b in range(len(B) + 1):
                if a - 1 >= 0 and b - 1 >= 0 and A[a - 1] == B[b - 1]:
                    f[a][b] = 1 + f[a - 1][b - 1]
                    ans = max(ans, f[a][b])
                        
        return ans
        '''
        2/2 Binary search
        Sort of brute force by checking each possible length.
        '''
        def check(length):
            seen = {A[i:i+length]
                    for i in range(len(A) - length + 1)}
            return any(B[j:j+length] in seen
                       for j in range(len(B) - length + 1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1