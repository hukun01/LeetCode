# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
class Solution:
    def modifyString(self, s: str) -> str:
        '''
        Array.
        A useful observation is that 3 candidate letters would be
        enough to ensure non consecutive repeating chars. Hence we
        just use 'abc', and for each '?', we pick the one from 'abc'
        that's different than the prev and the next chars.
        '''
        candidates = set('abc')
        ans = []
        prev = ''
        for i, c in enumerate(s):
            nex = s[i+1] if i+1 < len(s) else '?'
            cur = c if c != '?' else (candidates - {prev, nex}).pop()
            ans.append(cur)
            prev = cur
        return ''.join(ans)