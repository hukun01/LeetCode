# 115. Distinct Subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        DP. 
        Overall, DP is often a natural fit for string problems
        about subsequence count or match.
        
        f[i][j] is number of distinct subsequences in t[:i] and s[:j].
        
        Transitions:
        f[i+1][j+1] = f[i+1][j], if t[i] != s[j], this means that
        s[j] is not useful for matching, we have to find a solution
        for t[:i+1] (include t[i]) from s[:j] (exclude s[j]);
        
        f[i+1][j+1] = f[i+1][j] + f[i][j], if t[i] == s[j], this means
        that we can take s[j], or not. 
        When we don't take s[j], same as the first transition.
        When we take s[j], we add to solution with the number by
        matching t[:i] from s[:j].
        
        We need to initiate the first row with 1 because when t is
        empty, an empty s can contain it once.
        
        '''
        S, T = len(s), len(t)
        f = [[0] * (S + 1) for _ in range(T + 1)]
        f[0] = [1] * (S + 1)
        for i in range(T):
            for j in range(S):
                if t[i] == s[j]:
                    f[i+1][j+1] = f[i + 1][j] + f[i][j]
                else:
                    f[i+1][j+1] = f[i + 1][j]
        return f[-1][-1]