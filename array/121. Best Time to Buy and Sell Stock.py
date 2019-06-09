class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currMin = float('inf') # don't use max(prices) due to empty input
        for p in prices:
            currMin = min(currMin, p)
            currProfit = p - currMin
            maxProfit = max(maxProfit, currProfit)
        return maxProfit