# 243. Shortest Word Distance
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ans = inf
        seen = {}
        targets = {word1:word2, word2:word1}
        for i, w in enumerate(words):
            if w in targets and targets[w] in seen:
                ans = min(ans, i - seen[targets[w]])
            seen[w] = i
        return ans