# 243. Shortest Word Distance
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ans = inf
        i1 = i2 = None
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
            elif w == word2:
                i2 = i
            if i1 != None and i2 != None:
                ans = min(ans, abs(i1 - i2))
        return ans