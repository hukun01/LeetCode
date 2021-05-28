# 1216. Valid Palindrome III
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        '''
        LCS.
        Similar to 516. Longest Palindromic Subsequence, we find the longest
        palindromic subsequence p in s, then just check if len(s) - p <= k.

        The longest palindromic subsequence is the longest common subsequence
        between s and its reverse.

        Time: O(n^2)
        Space: O(n)
        '''
        n = len(s)
        def lcs(s0, s1):
            f = [0] * (n + 1)
            for i in range(1, n + 1):
                f1 = [0] * (n + 1)
                for j in range(1, n + 1):
                    if s0[i-1] == s1[j-1]:
                        f1[j] = f[j-1] + 1
                    f1[j] = max(f1[j], max(f[j], f1[j-1]))
                f = f1
            return f[n]

        lcs_len = lcs(s, s[::-1])
        return n - lcs_len <= k