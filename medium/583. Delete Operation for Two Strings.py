# 583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        DP.
        Overall, DP is often a natural fit for string problems
        about subsequence count or match.
        
        To find the min distance, we need to find the length of
        longest common subsequence (LCS) between w1 and w2.
        
        Let f[i1][i2] be the length of LCS between w1[:i1] and w2[:i2].
        
        Transitions:
        if w1[i1-1] == w2[i2-1]:
            f[i1][i2] = f[i1-1][i2-1] + 1
        else:
            f[i1][i2] = max(f[i1-1][i2], f[i1][i2-1]).
            Here we skip w1[i1-1] or w2[i2-1] if w1[i1-1] != w2[i2-1].
        
        Then ans = len(w1) - lcsLen + len(w2) - lcsLen
        
        Note that f[i] only depends on f[i-1], so space complexity can be reduced to
        O(n) where n is the length of the shorter string.
        '''
        w1, w2 = word1, word2
        l1, l2 = len(w1), len(w2)
        f = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i1 in range(1, l1 + 1):
            for i2 in range(1, l2 + 1):
                if w1[i1-1] == w2[i2-1]:
                    f[i1][i2] = f[i1-1][i2-1] + 1
                else:
                    f[i1][i2] = max(f[i1-1][i2], f[i1][i2-1])
        lcsLen = f[-1][-1]
        return l1 - lcsLen + l2 - lcsLen