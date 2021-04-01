class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        1/2 DP.

        Let f[i] be whether we can break s[:i].
        f[0] = True
        f[i] = any(f[j] and s[j:i] in wordDict for j in range(i))
        answer is f[n], where n is len(s)

        Time: O(n^2)
        Space: O(n)
        '''
        wordDict = set(wordDict)
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        for i in range(1, n + 1):
            f[i] = any(f[j] and s[j:i] in wordDict for j in range(i))

        return f[-1]

        '''
        2/2 Memoized DFS

        The dfs method returns whether s[start:] be broken into words.

        '''
        wordDict = set(wordDict)
        n = len(s)
        @cache
        def dfs(start):
            if start == n:
                return True
            for end in range(start + 1, n + 1):
                if s[start: end] in wordDict and dfs(end):
                    return True
            return False
        return dfs(0)