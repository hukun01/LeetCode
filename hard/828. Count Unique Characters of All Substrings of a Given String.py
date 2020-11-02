# 828. Count Unique Characters of All Substrings of a Given String
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        '''
        2/2 Naive but straightforward array approach.
        For each char c, we find the range in which c is the unique char,
        by scanning left and right. Then add ans by left_count * right_count.

        Time O(nk) where n is the length of s, and k is # of unique chars.
        Space O(1).
        '''
        MOD = 10 ** 9 + 7
        ans = 0
        n = len(s)
        for i, c in enumerate(s):
            l = i - 1
            while l >= 0 and s[l] != c:
                l -= 1
            r = i + 1
            while r < n and s[r] != c:
                r += 1
            ans += (i - l) * (r - i)
        return ans % MOD
        '''
        2/2 Optimized array approach.
        For each char c, we still find the range in which c is the unique char,
        and add ans by left_count * right_count. However, instead of scanning
        left and right repeatedly, keep track of the last two occurances
        (l1, l2) of each char. When seeing the third occurance i, add to ans
        (l2 - l1) * (i - l2), and update (l1, l2) to be (l2, i).
        Note that the initial values of the last two occurances are [-1, -1],
        and we need to wrap up the calculation with (l2 - l1) * (n - l2).

        Time O(n + k).
        Space O(k).
        '''
        MOD = 10 ** 9 + 7
        index = defaultdict(lambda: [-1, -1])
        res = 0
        n = len(s)
        for i, c in enumerate(s):
            l1, l2 = index[c]
            res += (l2 - l1) * (i - l2)
            index[c] = [l2, i]
        for c in index:
            l1, l2 = index[c]
            res += (l2 - l1) * (n - l2)
        return res % MOD