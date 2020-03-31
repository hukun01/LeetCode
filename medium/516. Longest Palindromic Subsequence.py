# 516. Longest Palindromic Subsequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        Let f[i][j] be the length of the longest palindrome in
        s[i:j].
        Transitions:
        f[i][j] = f[i+1][j-1] + 2, if s[i] == s[j], in this case we
        take the chars from both sides;
        f[i][j] = max(f[i][j-1], f[i+1][j]), if s[i] != s[j], in this
        case we take the longer palindrome from either dropping \
        the right char or the left char.
        
        Note that f[i][i] = 1.
        A key is that we have to start i from n-1 to 0, because
        the longer palindrome can only be built from a shorter one.
        '''
        if s == s[::-1]: 
            return len(s)
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            f[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] + 2
                else:
                    f[i][j] = max(f[i][j-1], f[i+1][j])
        return f[0][n-1]