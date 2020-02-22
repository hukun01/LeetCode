# 1358. Number of Substrings Containing All Three Characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        Sliding window.

        Record the last index of each element.
        The starting index of a substring is in [0, min(last.values())],
        the ending index is 'i', but we don't use 'i' directly.
        So at each ending index 'i', the number of substrings is
        1 + min(last.values()).
        '''
        last = { 'a': -1, 'b': -1, 'c': -1 }
        ans = 0
        for i, c in enumerate(s):
            last[c] = i
            ans += 1 + min(last.values())
        return ans