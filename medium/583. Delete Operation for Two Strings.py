# 583. Delete Operation for Two Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        DP.
        Overall, DP is often a natural fit for string problems
        about subsequence count or match.
        
        To find the min distance, we need to find the longest common subsequence
        between w1 and w2.
        
        Let f[i][j] be the length of longest subseq in w1[:i] that appears in w2[:j].
        
        Transitions:
        f[i][j] = max(f[i-1][j-1] + 1, max(f[i-1][j], f[i][j-1])).
        First option is we take w1[i-1] and w2[j-1] if w1[i-1] == w2[j-1];
        Second option is we skip w1[i-1] or w2[j-1] if w1[i-1] != w2[j-1].
        
        Then ans = len(w1) - max(f[-1]) + len(w2) - max(f[-1])
        
        Note that f[i] only depends on f[i-1], so space complexity can be reduced to
        O(n) where n is the length of the shorter string.
        '''
        w1, w2 = word1, word2
        f = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]
        for i in range(1, len(w1) + 1):
            for j in range(1, len(w2) + 1):
                if w1[i-1] == w2[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])
        commonLen = f[-1][-1]
        return len(w1) - commonLen + len(w2) - commonLen