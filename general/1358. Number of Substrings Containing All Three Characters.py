# 1358. Number of Substrings Containing All Three Characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        Sliding window.

        Record the last index of each element.
        A substring is defined by [startIdx, i]. At each index i, we find
        the number of startIdx, which will be the number of substrings.
        The range of startIdx is [0, min(last.values())], with last initialized
        by -1 for each element. This will cover the scenarios when we don't find
        all elements yet.
        Hence the number of substrings is 1 + min(last.values()).
        '''
        last = { 'a': -1, 'b': -1, 'c': -1 }
        ans = 0
        for i, c in enumerate(s):
            last[c] = i
            ans += 1 + min(last.values())
        return ans