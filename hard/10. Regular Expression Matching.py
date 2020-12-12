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
        def isMatched(m, n):
            result = False
            if n == -1:
                result = m == -1
            elif m >= 0 and p[n] in (s[m], '.'):
                result |= isMatched(m-1, n-1)
            elif p[n] == '*':
                result |= isMatched(m, n-2) # 'a*' counts as empty
                if m >= 0 and p[n-1] in (s[m], '.'):
                    result |= isMatched(m-1, n)
            return result
        
        return isMatched(len(s)-1, len(p)-1)