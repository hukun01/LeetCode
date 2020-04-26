# 1422. Maximum Score After Splitting a String
class Solution:
    def maxScore(self, s: str) -> int:
        '''
        Count the number of 1s in s, and scan s. Every time we
        see a '0', increase zero counter; when seeing a '1',
        decrease one counter. Calculate the max answer during scan.
        
        Note that to keep both substrings non-empty, we can't
        take the last char into left substring.
        '''
        count = collections.Counter(s)
        count['0'] = 0
        ans = 0
        for c in s[:-1]:
            if c == '0':
                count[c] += 1
            else:
                count[c] -= 1
            ans = max(ans, count['0'] + count['1'])
        return ans