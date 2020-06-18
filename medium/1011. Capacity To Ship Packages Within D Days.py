# 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        '''
        We know the capacity ranges from [max(weights), inf], so we can try different
        capacity with binary search, and find the minimal one that satisfies the requirements.
        Similar to 875. Koko Eating Bananas, and 5455. Minimum Number of Days to Make m Bouquets.
        '''
        l, h = max(weights), sum(weights)
        def isGood(capacity):
            days = 0
            loaded = 0
            for w in weights:
                loaded += w
                if loaded > capacity:
                    days += 1
                    loaded = w
            return days + 1 <= D
            
        while l < h:
            m = (l + h) // 2
            if isGood(m):
                h = m
            else:
                l = m + 1
        return l