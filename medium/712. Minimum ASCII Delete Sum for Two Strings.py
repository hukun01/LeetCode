# 712. Minimum ASCII Delete Sum for Two Strings
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        DP.
        Overall, DP is often a natural fit for string problems
        about subsequence count or match.

        Let f[i][j] be the max sum of common subseq between s1[:i] and s2[:j].

        Transitions:
        f[i][j] = max(f[i-1][j-1] + 1, max(f[i-1][j], f[i][j-1])).
        First option is we take w1[i-1] and w2[j-1] if w1[i-1] == w2[j-1];
        Second option is we skip w1[i-1] or w2[j-1] if w1[i-1] != w2[j-1].

        f[-1][-1] is the max sum of common subseq between s1 and s2, and the min deleted
        sum is obvious now.
        
        Note that f[i] only depends on f[i-1], so space complexity can be reduced to
        O(n) where n is the length of the shorter string.
        '''
        f = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    f[i][j] = f[i-1][j-1] + ord(s1[i-1])
                else:
                    f[i][j] = max(f[i][j-1], f[i-1][j])

        def count(s):
            return sum(ord(c) for c in s)
        total = count(s1) + count(s2)
        return total - f[-1][-1] * 2