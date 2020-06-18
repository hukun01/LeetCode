# 5455. Minimum Number of Days to Make m Bouquets
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        If the total days >= m * k, there must be an answer, we just need to find the
        minimal days. Knowing the days ranges from [1, max(bloomDay)], we can try
        different days with binary search.
        Similar to 875. Koko Eating Bananas, and 1011. Capacity To Ship Packages Within D Days.
        '''
        if m * k > len(bloomDay):
            return -1
        l = min(bloomDay)
        h = max(bloomDay)
        
        def isGood(day):
            count = 0
            bouquets = 0
            for d in bloomDay:
                if day >= d:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquets += 1
                    count = 0

            return bouquets >= m
            
        while l < h:
            mid = (l + h) // 2
            if isGood(mid):
                h = mid
            else:
                l = mid + 1
        return h