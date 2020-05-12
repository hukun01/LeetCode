# 1358. Number of Substrings Containing All Three Characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        Sliding window.
        1/2
        Record the last index of each element.
        A substring is defined by [startIdx, i]. At each index i, we find
        the number of startIdx, which will be the number of substrings.
        The range of startIdx is [0, min(last.values())], with last initialized
        with -1 for each element. Defaults will cover the scenarios when we haven't
        find all elements yet.
        Hence the number of substrings is 1 + min(last.values()).
        '''
        last = { 'a': -1, 'b': -1, 'c': -1 }
        ans = 0
        for i, c in enumerate(s):
            last[c] = i
            ans += 1 + min(last.values())
        return ans
        '''
        2/2 A more straightforward way of sliding window.
        '''
        startIdx = 0
        ans = 0
        seen = { c: 0 for c in 'abc' }
        for c in s:
            seen[c] += 1
            while all(seen.values()):
                seen[s[startIdx]] -= 1
                startIdx += 1
            ans += startIdx
        return ans