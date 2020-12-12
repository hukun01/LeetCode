# 730. Count Different Palindromic Subsequences
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        '''
        Let dp[s][e] be the answer for S[s: e], including s, excluding e.
        dp[s][e] is the sum of dp[i+1][j] + (1, if i == j; 2, otherwise)
        for every i and j, where i is the first index of char in S[s: e], j
        is the last index of this char. The chars can be one of 'abcd'.
        
        Basically we are looking for strings in format: 
        str  "a_a" where '_' can be any chars including empty. (See index next line)
        index i j.
        If i == j, means we only have "_a_", this is 1 palindrome,
        if i != j, means we have "a_a", this is 2 palindromes, as '_' can be any chars, or empty.
        '''
        @lru_cache(None)
        def dp(s, e):
            count = 0
            for c in 'abcd':
                try:
                    i = S.index(c, s, e)
                    j = S.rindex(c, s, e)
                except ValueError:
                    continue
                count += dp(i + 1, j) + 1 + (i != j)
            return count
        return dp(0, len(S)) % (10 ** 9 + 7)