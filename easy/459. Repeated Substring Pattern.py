# 459. Repeated Substring Pattern
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        KMP.
        If the input string s consists of repeated pattern p, then we can
        treat it as 'pp...pp'.
        The lps table from KMP helps identify the proper prefix which is the
        substrings in [] of '[pp..p]p' and 'p[p..pp]'.
        The length of 'p' is 'n - lps[-1]', we just need to ensure it is not 0,
        and can divide n, this is to ensure the common prefix and suffix do not
        share substrings that can't be formed by 'p'.
        s:  p  x..x p
            A   B   C

        s:  p  x..x p
            D   E   F
        Now we know:
            B's suffix == E's suffix, they are literally the same parts of s.
            B's suffix == F, per lps
        then we know:
            E's suffix == F

        We just found a recurring part from B and E. Now we can push this from
        right to left, as long as (A + B + C) can be divided by p, answer would
        be True.

        If the input string is not in 'pp..pp' format, the lps table will look
        different, for example, '[p]xyzp' and 'pxyz[p]'. In this case, pattern
        length 'n - lps[-1]' will be length of 'pxyz', which can't be repeated.

        Time: O(n)
        Space: O(n)
        '''
        def build_lps(s):
            n = len(s)
            lps = [0] * n
            for i in range(1, n):
                k = lps[i - 1]
                while k > 0 and s[k] != s[i]:
                    k = lps[k - 1]

                if s[k] == s[i]:
                    lps[i] = k + 1

            return lps

        lps = build_lps(s)
        n = len(s)
        pattern_size = n - lps[n - 1]
        return pattern_size != 0 and n % pattern_size == 0