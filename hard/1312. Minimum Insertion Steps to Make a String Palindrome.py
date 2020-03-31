# 1312. Minimum Insertion Steps to Make a String Palindrome
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Find the longest subseq that is palindrome,
        the rest needs to be mirrored.
        
        Same as 516. Longest Palindromic Subsequence.
        '''
        n = len(s)
        def longestPalindromeSubseq(s):
            if s == s[::-1]: 
                return len(s)
            f = [[0] * n for _ in range(n)]
            for i in range(n-1, -1, -1):
                f[i][i] = 1
                for j in range(i+1, n):
                    if s[i] == s[j]:
                        f[i][j] = f[i+1][j-1] + 2
                    else:
                        f[i][j] = max(f[i][j-1], f[i+1][j])
            return f[0][n-1]
        return n - longestPalindromeSubseq(s)