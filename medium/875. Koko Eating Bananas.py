# 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        '''
        Binary search the value spaces.

        The key is to reduce the search space.
        The naive search space is [1, max(piles)], but can be improved.

        The best case defines the lower bound, in which every pile is
        identical, so the lower bound is ceil(sum(piles) / H).

        The worst case defines the upper bound, 
        which is like [1,1,1,...,big_num], in which most of the hours are
        wasted, except the only one with big_num, so we use *total to estimate
        the *big_num, and ignore the tiny numbers, but considering that we've
        spent the hours on the tiny numbers.
        Thus, the upper bound should be ceil(sum(piles) / (H - (len(piles) - 1))).

        Time: O(log V) where V is the value range defined by piles and H.
        Space: O(1)
        '''
        total = sum(piles)
        l = ceil(total / H)
        h = ceil(total / (H - len(piles) + 1))
        while l < h:
            m = (l + h) // 2
            if sum(ceil(pile / m) for pile in piles) <= H:
                h = m
            else:
                l = m + 1
        return l