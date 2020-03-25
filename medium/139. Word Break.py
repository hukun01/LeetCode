class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        1/2 Dynamic Programming

        dp[0] = True
        dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
        '''
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))

        return dp[-1]

        '''
        2/2 Recursion with Memoization

        Ending with index 'idx', can the string be broken into recognized words.

        '''
        wordDict = set(wordDict)
        @functools.lru_cache(None)
        def dfs(start):
            if start == len(s):
                return True
            for i in range(start + 1, len(s) + 1):
                if s[start: i] in wordDict and dfs(i):
                    return True
            return False
        return dfs(0)