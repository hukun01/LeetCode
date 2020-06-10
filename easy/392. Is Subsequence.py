# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIdx = tIdx = 0
        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] == t[tIdx]:
                sIdx += 1
            tIdx += 1
        return sIdx == len(s)