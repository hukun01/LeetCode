# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_so_far = math.inf # don't use max(prices) due to empty input
        for p in prices:
            min_so_far = min(min_so_far, p)
            ans = max(ans, p - min_so_far)
        return ans