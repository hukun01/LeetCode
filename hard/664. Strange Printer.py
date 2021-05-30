# 664. Strange Printer
class Solution:
    def strangePrinter(self, s: str) -> int:
        '''
        Interval DP.
        Let dp[i, j] be the answer for s[i:j+1], we have
        dp[i, j] = min(dp[i, m-1] + dp[m+1, j]), where m is the index of s[i]
        between (i, j].
        This basically means we try to print s[i, m] using s[i], because we
        have to print out s[i], so trying to print more and see if it can cover
        more indexes. And we process s[m+1, j+1], and leave s[m] = s[i].
        We check every index of s[i] between (i, j] instead of all index in
        this range, because it doesn't help to print s[i] if there's no
        existing s[i] in those sub-ranges.

        Another optimization is to merge the same chars in s into one, as that
        doesn't change the number of turns needed.

        Time: O(n^3) where n is len(s)
        Space: O(n^2)
        '''
        s = [c for i, c in enumerate(s) if i == 0 or c != s[i-1]]

        indexes = defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)

        @cache
        def dp(i, j):
            if i > j:
                return 0

            ans = 1 + dp(i+1, j) # default is to print every char one by one.
            c = s[i]
            k = bisect_right(indexes[c], i)
            while k < len(indexes[c]) and indexes[c][k] <= j:
                m = indexes[c][k]
                ans = min(ans, dp(i, m-1) + dp(m+1, j))
                k += 1

            return ans


        return dp(0, len(s)-1)