# 914. X of a Kind in a Deck of Cards
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        Brute force.

        Use a Counter object to help the term-frequency part, (note that Counter is a subclass of Dict)
        then the X will be in [2, minCardsCount]. 
        Simply try all the X for all cards counts, if all of the cards counts
        can be divided by X, we are good, otherwise, try the next X.

        Assume n is the total number of cards, this is O(n) time, O(n) space,
        as the nested for-loop has totally (minCardsCount * keyCount) steps, which is less or equal to n.
        """
        cardsCount = Counter(deck)
        for X in range(2, min(cardsCount.values()) + 1):
            if all(c % X == 0 for c in cardsCount.values()):
                return True
        return False