# 516. Longest Palindromic Subsequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        1/4 LCS.
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
        
        return lcs(s, s[::-1])
        '''
        2/4 Interval DP, transition function 1.
        Let f[i][j] be the length of the longest palindrome in s[i:j].
        Transitions:
        f[i][j] = f[i+1][j-1] + 2, if s[i] == s[j], in this case we take the
        chars from both sides;
        f[i][j] = max(f[i][j-1], f[i+1][j]), if s[i] != s[j], in this case we
        take the longer palindrome from either dropping the right char or the
        left char.

        Note that f[i][i] = 1.
        This is a prime example of interval DP, where we build the solutions
        for small intervals, and build soutions for larger intervals based on
        those small solutions.

        Time: O(n^2)
        Space: O(n^2)
        '''
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1

        for size in range(2, n + 1):
            for i in range(n + 1 - size):
                j = i + size - 1
                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] + 2
                else:
                    f[i][j] = max(f[i][j-1], f[i+1][j])

        return f[0][n - 1]
        '''
        3/4 Interval DP, transition function 2.
        The transition function includes the 'size' and the starting point 'i'.
        These 2 fields will fix the ending point 'j', so essentially it's the
        same as 2/4. It will be more useful in 4/4.

        Time: O(n^2)
        Space: O(n^2)
        '''
        n = len(s)
        ans = 1
        f = [[0] * n for _ in range(n+1)]
        for i in range(n):
            f[1][i] = 1

        for size in range(2, n + 1):
            for i in range(n + 1 - size):
                j = i + size - 1
                if s[i] == s[j]:
                    f[size][i] = f[size - 2][i+1] + 2
                else:
                    f[size][i] = max(f[size - 1][i], f[size - 1][i+1])

                ans = max(ans, f[size][i])

        return ans
        '''
        4/4 Interval DP, optmized space.
        From 3/4, we can see that the f[size] depends on f[size-2] or f[size-1].
        This means we only need 3 rolling 1d arrays at any time to capture all
        states.

        Time: O(n^2)
        Space: O(n)
        '''
        n = len(s)
        ans = 1
        f0 = [0] * n
        f1 = [1] * n

        for size in range(2, n + 1):
            f2 = [0] * n
            for i in range(n + 1 - size):
                j = i + size - 1
                if s[i] == s[j]:
                    f2[i] = f0[i+1] + 2
                else:
                    f2[i] = max(f1[i], f1[i+1])

                ans = max(ans, f2[i])
            f0, f1 = f1, f2

        return ans