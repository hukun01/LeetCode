class Solution:
    def minEatingSpeed(self, piles, H):
        """
        Another instance for binary searching the value spaces.
        
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def possible(piles, k, H):
            # Alternatively, use (p-1) // k to get a smaller division result, and +1 to it to make a ceiling.
            return sum(math.ceil(p / k) for p in piles) <= H
        
        l, h = 1, max(piles)
        while l < h:
            mid = (l + h) // 2
            if possible(piles, mid, H):
                h = mid
            else:
                l = mid + 1
        return l