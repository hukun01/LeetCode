# 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Compare every pair of adjacent words.
        We can compare integer lists like [1, 2] < [1, 3].
        Time: O(WN) where W is the number of words, N is the length of the
        longest word.
        Space: O(N)
        This can be updated to compare char by char for w1 and w2 to achieve
        O(1) space, in case N is huge.
        '''
        orderMap = { char: idx for idx, char in enumerate(order) }
        for w1, w2 in zip(words, words[1:]):
            if [orderMap[c] for c in w1] > [orderMap[c] for c in w2]:
                return False
        return True