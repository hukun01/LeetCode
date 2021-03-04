# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Compare every pair of adjacent words.
        We can compare integer lists like [1, 2] < [1, 3].
        Time: O(WN) where W is the number of words, N is the length of the
        longest word.
        Space: O(1) as there are at most 26 letters.
        '''
        pos = {c: i for i, c in enumerate(order)}
        pos[None] = -inf
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip_longest(w1, w2):
                if c1 == c2:
                    continue
                if pos[c1] > pos[c2]:
                    return False
                break

        return True