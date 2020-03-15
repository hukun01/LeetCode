# 309. Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        There are 3 states that record the current profit:
        empty: empty hand, can buy/rest.
        hold: hold(bought) one stock, can sell/rest, can't buy again.
        sold: sold one stock, have to rest and become empty.

        The transitions are as below:
        empty -> (rest) -> empty
        empty -> (buy)  -> hold
        hold -> (rest) -> hold
        hold -> (sell) -> sold
        sold -> (rest) -> empty
        '''
        if not prices:
            return 0
        N = len(prices)
        empty = [0] * N
        hold = [0] * N
        sold = [0] * N
        
        hold[0] = -prices[0]
        sold[0] = -float('inf')
        for i in range(1, N):
            empty[i] = max(empty[i - 1], sold[i - 1])
            hold[i] = max(hold[i - 1], empty[i - 1] - prices[i])
            sold[i] = hold[i - 1] + prices[i]
        return max(empty[-1], sold[-1])