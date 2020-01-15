# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Compare every pair of adjacent words.
        Tips: we can compare integer lists like [1, 2] < [1, 3].
        '''
        orderMap = { char: idx for idx, char in enumerate(order) }
        words = [[orderMap[c] for c in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))