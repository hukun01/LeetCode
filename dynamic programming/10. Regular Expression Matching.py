class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Search with memoization with below scenarios:
        If p[n] == s[m] or p[n] == '.': dp[m][n] = dp[m-1][n-1];
        If p[n] == '*': 
            dp[m][n] = dp[m][n-2] OR below // a* only counts as empty
            if p[n-1] == s[m] or p[n-1] == '.':
                dp[m][n] = dp[m-1][n]      // a* counts as 1+ a
        '''
        matched = dict()
        def isMatched(m, n):
            if (m, n) in matched:
                return matched[(m, n)]
            result = False
            if n == -1:
                result = m == -1
            elif m >= 0 and p[n] in (s[m], '.'):
                result |= isMatched(m-1, n-1)
            elif p[n] == '*':
                result |= isMatched(m, n-2) # 'a*' counts as empty
                if m >= 0 and p[n-1] in (s[m], '.'):
                    result |= isMatched(m-1, n)
            matched[(m, n)] = result
            return result
        
        return isMatched(len(s)-1, len(p)-1)