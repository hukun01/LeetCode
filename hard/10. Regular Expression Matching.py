# 10. Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Search with memoization with below scenarios:
        if p[n] in (s[m], '.'): dp[m][n] = dp[m-1][n-1]
        elif p[n] == '*': dp[m][n] = dp[m][n-2] or // a* counts as empty
            if p[n-1] in (s[m], '.'): dp[m][n] = dp[m-1][n] // a* counts as one or more a
        '''
        @lru_cache(None)
        def match(m, n):
            ans = False
            if n == -1:
                ans = m == -1
            elif m >= 0 and p[n] in (s[m], '.'):
                ans |= match(m-1, n-1)
            elif p[n] == '*':
                ans |= match(m, n-2) # 'a*' counts as empty
                if m >= 0 and p[n-1] in (s[m], '.'):
                    ans |= match(m-1, n)
            return ans
        
        return match(len(s)-1, len(p)-1)