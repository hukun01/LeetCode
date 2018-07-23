class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def possible(piles, k, H):
            # Use (p-1) // k to get a smaller division result, and +1 to it to make a ceiling.
            return sum((p - 1) // k + 1 for p in piles) <= H
        
        l, h = 1, max(piles)
        while l < h:
            mid = (l + h) // 2
            if possible(piles, mid, H):
                h = mid
            else:
                l = mid + 1
        return l