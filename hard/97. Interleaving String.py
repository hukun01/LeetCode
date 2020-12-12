# 97. Interleaving String
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Similar to 10. Regular Expression Matching.
        Match from the tail, and cache all seen positions in s1 and s2.
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache(None)
        def match(i1, i2):
            if i1 == -1 and i2 == -1:
                return True
            ans = False
            i3 = i1 + i2 + 1
            if i1 >= 0 and s1[i1] == s3[i3]:
                ans |= match(i1 - 1, i2)
            if i2 >= 0 and s2[i2] == s3[i3]:
                ans |= match(i1, i2 - 1)
            return ans
        return match(len(s1) - 1, len(s2) - 1)