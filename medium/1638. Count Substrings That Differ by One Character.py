# 1638. Count Substrings That Differ by One Character
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        '''
        Array.
        Compare each char from s and t, for each unmatched char c, find the
        range in which c is the only unmatched char, and add ans by
        left_count * right_count.
        Instead of repeatedly scanning left and right for each unmatched char,
        keep track of current matched chars after c in 'cur', and the previous
        matched chars before c in 'pre'. Keep adding 'pre' to ans, aka, adding
        left_count to ans for right_count times.
        For example, in 'MUMM' where 'M' means matched, 'U' means unmatched,
        the number of substrings is 2(cutting 1 'M') * 3 (cutting 2 'M's). The
        'pre' would be 0 initially, until 'cur' become 2 when we are at 'U',
        then we update (pre, cur) to be (cur, 0), and add 'pre' to ans, for
        another 'cur' times which is 3.

        Similar to 828. Count Unique Characters of All Substrings of a Given String
        '''
        s_len, t_len = len(s), len(t)
        def count(s_start, t_start):
            ans = pre = cur = 0
            for k in range(min(s_len - s_start, t_len - t_start)):
                cur += 1
                if s[s_start + k] != t[t_start + k]:
                    pre, cur = cur, 0
                ans += pre
            return ans
        return sum(count(i, 0) for i in range(s_len)) + sum(count(0, j) for j in range(1, t_len))