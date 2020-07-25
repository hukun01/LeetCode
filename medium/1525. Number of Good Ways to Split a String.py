# 1525. Number of Good Ways to Split a String
class Solution:
    '''
    Prefix sum.
    Count the total char-frequency 'total', and iterate through s,
    keep removing each char from 'total', and add it to the 'cur'
    set. Once the size of 'cur' equals to that of 'total', it's a
    good split.
    '''
    def numSplits(self, s: str) -> int:
        total = Counter(s)
        total_count = len(total)
        cur = set()
        ans = 0
        for c in s:
            cur.add(c)
            total[c] -= 1
            total_count -= 0 == total[c]
            ans += len(cur) == total_count
        return ans