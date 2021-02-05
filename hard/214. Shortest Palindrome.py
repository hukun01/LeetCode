# 214. Shortest Palindrome
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        1/2 Rabin Karp, or rolling hash.
        This problem can be transformed into another one that finds the longest
        palindromic prefix. After this prefix is found, we just append the
        reversed non-overlapped suffix to the head.

        Now the key is to quickly check whether the s[:i + 1] is palindromic
        for each i. We use rolling hash technique, this is similar to how we
        use this technique in 1392. Longest Happy Prefix.

        Time: O(n)
        Space: O(n) considering output.
        '''
        R = 128
        mod = 10 ** 9 + 7
        p = 1
        h1 = h2 = 0
        ans = -1
        for i, c in enumerate(s):
            h1 = (h1 * R + ord(c)) % mod
            h2 = (h2 + p * ord(c)) % mod
            if h1 == h2 and s[:i + 1] == s[:i + 1][::-1]:
                ans = i + 1
            p = (p * R) % mod

        return s[ans:][::-1] + s
        '''
        2/2 KMP.
        The same idea transformation can be leveraged in a different way.
        Note that in KMP we build the 'fail' table to help us move the pattern
        pointer back smartly, that table helps here.

        See more details about KMP in 28. Implement strStr()

        To find the max 'palin' in [palin]xxx, we build the 'fail' table in
        this string t [palin]xyz#zyx[palin], in which fail[-1] would be the
        max length of proper prefix for the whole 't'.
        Note that we need to insert a '#' in the middle to ensure that the
        max fail[i] <= len(s).

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

        lps = build_lps(s + '#' + s[::-1])

        return s[lps[-1]:][::-1] + s