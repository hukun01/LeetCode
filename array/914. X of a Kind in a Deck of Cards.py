class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        
        Kind of brute force, but surprisingly good in terms of time and space.

        Use a Counter object to help the term-frequency part, (note that Counter is a subclass of Dict)
        then the X will be in [2, minCardsCount]. 
        Simply try all the X for all cards counts, if all of the cards counts
        can be divided by X, we are good, otherwise, try the next X.

        Assume n is the total number of cards, this is O(n) time, O(n) space,
        as the nested for-loop has (minCardsCount * keyCount) steps, which is less or equal to n.
        """
        cardsCount = collections.Counter(deck)
        for X in range(2, min(cardsCount.values()) + 1):
            if all([c % X == 0 for c in cardsCount.values()]):
                return True
        return False