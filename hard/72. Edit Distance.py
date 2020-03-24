# 72. Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = word1, word2
        
        @functools.lru_cache(None)
        def match(i1, i2):
            if i1 == -1:
                return i2 + 1
            if i2 == -1:
                return i1 + 1

            if w1[i1] == w2[i2]:
                return match(i1 - 1, i2 - 1)
            else:
                return min( match(i1, i2 - 1),          # insert to w1[i1]
                            match(i1 - 1, i2),          # delete w1[i1]
                            match(i1 - 1, i2 - 1)) + 1  # replace w1[i1]
        return match(len(w1) - 1, len(w2) - 1)