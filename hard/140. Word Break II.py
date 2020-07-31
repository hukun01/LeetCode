# 140. Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        Memoized DFS.
        '''
        words = set(wordDict)
        @lru_cache(None)
        def words_end_in(i):
            if i == len(s):
                return [""]
            ans = []
            for j in range(i + 1, len(s) + 1):
                if (w := s[i:j]) in words:
                    for tail in words_end_in(j):
                        ans.append(f"{w} {tail}" if tail else w)
            return ans

        return words_end_in(0)