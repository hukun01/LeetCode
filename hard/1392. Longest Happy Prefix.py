# 1392. Longest Happy Prefix
class Solution:
    def longestPrefix(self, s: str) -> str:
        '''
        1/3 Rabin Karp, or Karp Rabin algorithm, also called rolling hash.
        See 28. Implement strStr() for more details.
        '''
        l = r = 0
        alphabet_size = 128
        pattern_hash = 1
        mod = 10 ** 9 + 7
        n = len(s)
        ans = 0
        for i in range(n - 1):
            l = (l * alphabet_size + ord(s[i])) % mod
            r = (r + pattern_hash * ord(s[n - 1 - i])) % mod
            pattern_hash = pattern_hash * alphabet_size % mod
            if l == r:
                ans = i + 1
        return s[0:ans]
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