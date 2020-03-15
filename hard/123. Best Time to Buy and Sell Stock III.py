# 123. Best Time to Buy and Sell Stock III
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        oneBuy tracks the min price so far, and
        oneBuyOneSell tracks the current max profit.
        This is the same as the 121. Best Time to Buy and Sell Stock.
        
        Now twoBuy tracks the min price after we use our first
        profit in the next stock, and twoBuyTwoSell tracks the max
        profit with the 'discount' we get from the first sell.
        '''
        oneBuyOneSell = twoBuyTwoSell = 0
        oneBuy = twoBuy = float('inf')
        for p in prices:
            oneBuy = min(oneBuy, p)
            oneBuyOneSell = max(oneBuyOneSell, p - oneBuy)
            twoBuy = min(twoBuy, p - oneBuyOneSell)
            twoBuyTwoSell = max(twoBuyTwoSell, p - twoBuy)
            
        return twoBuyTwoSell