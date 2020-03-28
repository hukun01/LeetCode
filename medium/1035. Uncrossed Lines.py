# 1035. Uncrossed Lines
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        '''
        DP.
        Actually a LCS problem.

        f[i][j] is the max number of lines with A[:i] and B[:j]
        
        f[i][j] = f[i-1][j-1] + 1, if A[i-1] == B[j-1]
                = max(f[i-1][j], f[i][j-1]), otherwise
        '''
        f = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])
        return f[-1][-1]