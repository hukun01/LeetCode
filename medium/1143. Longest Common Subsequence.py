# 1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        DP.
        Overall, DP is often a natural fit for string problems about
        subsequence count or match.
        
        Let f[i][j] be the length of longest subsequence in w1[:i] and w2[:j].

        Transitions:
        f[i][j] = max(f[i-1][j-1] + 1, max(f[i-1][j], f[i][j-1])).
        First option is we take w1[i-1] and w2[j-1] if w1[i-1] == w2[j-1];
        Second option is we skip w1[i-1] or w2[j-1] if w1[i-1] != w2[j-1].

        Note that f[i] only depends on f[i-1], so space complexity can be reduced to
        O(n) where n is the length of the shorter string.
        '''
        w1, w2 = text1, text2
        f = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]
        for i in range(1, len(w1) + 1):
            for j in range(1, len(w2) + 1):
                if w1[i-1] == w2[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])

        return f[-1][-1]