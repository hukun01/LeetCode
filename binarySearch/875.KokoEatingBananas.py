class Solution:
    def minEatingSpeed(self, piles, H):
        """
        Another instance for binary searching the value spaces.
        
        The key is to reduce the search space.
        The naive search space is [1, max(piles)], but can be too big.
        
        The best case defines the lower bound, in which every pile is identical,
        so the lower bound is math.ceil(sum(piles) / H).
        
        The worst case defines the upper bound, 
        which is like [1,1,1,...,big_num], in which most of the hours are wasted,
        except the ones with big_num, so we use *total to estimate the *big_num, and ignore the 
        tiny numbers.
        Thus, the upper bound should be math.ceil(sum(piles) / (H - len(piles) + 1)).
        
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        total = sum(piles)
        l, h = math.ceil(total / H), math.ceil(total / (H - len(piles) + 1))
        while l < h:
            m = l + (h - l) // 2
            if sum(math.ceil(pile / K) for pile in piles) <= H:
                h = m
            else:
                l = m + 1
        return l