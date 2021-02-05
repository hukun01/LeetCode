# 1392. Longest Happy Prefix
class Solution:
    def longestPrefix(self, s: str) -> str:
        '''
        1/3 Rabin Karp, also called rolling hash.
        See 28. Implement strStr() for more details.
        '''
        l = r = 0
        R = 128
        power = 1
        mod = 10 ** 9 + 7
        n = len(s)
        ans = 0
        for i in range(n - 1):
            l = (l * R + ord(s[i])) % mod
            r = (r + power * ord(s[n - 1 - i])) % mod
            if l == r and s[:i + 1] == s[n - 1 - i:]:
                ans = i + 1
            power = power * R % mod
        return s[0: ans]
        '''
        2/3 KMP.
        The definition of longest happy prefix is literally the same as that of
        'fail' table in KMP. We just need to build the 'fail' table as part of
        KMP.

        See more details about KMP in 28. Implement strStr()

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

        return s[:lps[-1]]
        '''
        3/3 Z Algorithm.
        Use the original Z algorithm to compute the Z values, which at each
        index is the longest prefix length when comparing s[i:] and s.
        Whenever i and its z value x satisfy 'i + x == N', it means s[i:], the
        suffix, matches s' prefix. This is the longest happy prefix, because
        after i, the suffix can only get shorter.

        Time: O(N)
        Space: O(N)
        '''
        L = R = 0
        N = len(s)
        Z = [0] * N
        for i in range(1, N):
            if i > R:
                L = R = i
                while R < N and s[R - L] == s[R]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
            else:
                k = i - L
                if Z[k] < R - i:
                    Z[i] = Z[k]
                else:
                    L = i
                    while R < N and s[R - L] == s[R]:
                        R += 1
                    R -= 1
                    Z[i] = R - L + 1

        return next((s[i:] for i, x in enumerate(Z) if i + x == N), "")