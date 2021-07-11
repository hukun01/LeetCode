# 140. Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        1/2 Memoized DFS.
        '''
        words = set(wordDict)
        @cache
        def words_start_from(i):
            if i == len(s):
                return [""]
            ans = []
            for j in range(i + 1, len(s) + 1):
                if (w := s[i:j]) in words:
                    for tail in words_start_from(j):
                        ans.append(f"{w} {tail}" if tail else w)
            return ans

        return words_start_from(0)
        '''
        2/2 DFS backtrack.
        '''
        W = set(wordDict)
        ans = []
        n = len(s)
        def dfs(i, path):
            if i == n:
                ans.append(' '.join(path))
                return
            for j in range(i, n):
                part = s[i: j+1]
                if part in W:
                    path.append(part)
                    dfs(j + 1, path)
                    path.pop()

        dfs(0, [])
        return ans