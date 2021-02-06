# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
class Solution:
    def modifyString(self, s: str) -> str:
        '''
        Array.
        A useful observation is that 3 candidate letters would be
        enough to ensure non consecutive repeating chars. Hence we
        just use 'abc', and for each '?', we pick the one from 'abc'
        that's different than the prev and the next chars.

        Time: O(n)
        Space: O(n)
        '''
        arr = list(s)
        cands = set('abc')
        for i in range(len(arr)):
            if arr[i] == '?':
                left = arr[i-1] if i-1 >= 0 else None
                right = arr[i+1] if i+1 < len(arr) else None
                arr[i] = (cands - {left, right}).pop()

        return ''.join(arr)