# 243. Shortest Word Distance
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        '''
        Record the most recent positions for w1 and w2, and if they both exist,
        we do abs(i1 - i2).

        Time: O(nm) where n is len(words), m is len(w1 or w2)
        Space: O(1)
        '''
        ans = inf
        i1 = i2 = -1
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
            elif w == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))
        return ans