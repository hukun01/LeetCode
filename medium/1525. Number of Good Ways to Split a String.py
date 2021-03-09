# 1525. Number of Good Ways to Split a String
class Solution:
    '''
    Sliding window.
    Count the total char-frequency 'total', then iterate through s, using a
    sliding window to collect the seen chars, when a char's frequency == the
    total frequency, we know there's no such char on the right, and we can pop
    it out from 'total'. And whenever len(window) == len(total), we get a good
    split.

    Time: O(n) where n is len(s)
    Space: O(1) since there are at most 26 chars.
    '''
    def numSplits(self, s: str) -> int:
        total = Counter(s)
        window = Counter()
        ans = 0
        for a in s:
            window[a] += 1
            if window[a] == total[a]:
                total.pop(a)
            if len(window) == len(total):
                ans += 1
        return ans