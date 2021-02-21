# 1771. Maximize Palindrome Length From Subsequences
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        '''
        DP.
        Similar to 516. Longest Palindromic Subsequence.
        Finding palindromic subsequences from word1 and word2 is similar to
        finding them in 'word1+word2'. The difference here is that we need to
        find the two halves of the palindrome from word1 and word2 later.
        Reuse the method from 516 to get the dp array, and go through the i, j
        again to have i in [0, split) and j in [split, n), where split is
        len(word1).
        Note that to ensure both subsequences are non-empty, we also check
        s[i] == s[j].
        '''
        def longestPalinSubseq(s):
            n = len(s)
            f = [[0] * n for _ in range(n)]
            for i in range(n-1, -1, -1):
                f[i][i] = 1
                for j in range(i+1, n):
                    if s[i] == s[j]:
                        f[i][j] = f[i+1][j-1] + 2
                    else:
                        f[i][j] = max(f[i][j-1], f[i+1][j])
            return f

        s = word1 + word2
        f = longestPalinSubseq(s)
        split = len(word1)
        ans = 0
        for i in range(split):
            for j in range(split, len(s)):
                if s[i] == s[j]:
                    ans = max(ans, f[i][j])
        return ans