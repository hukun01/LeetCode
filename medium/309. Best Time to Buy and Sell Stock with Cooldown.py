# 309. Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        T[i][k][0] is the max profit with 0 stock after i-th day with k transactions.
        T[i][k][1] is the max profit with 1 stock after i-th day with k transactions.
        Since we can do any number of transactions, k doesn't matter, can be removed.
        T[0][0] = 0
        T[0][1] = -prices[0]
        
        Transitions:
        T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i])
        T[i-1][0] means rest from last day; T[i-1][1] + prices[i] means sell last stock.

        T[i][1] = max(T[i-1][1], T[i-2][0] - prices[i])
        T[i-1][1] means rest from last day; T[i-2][0] - prices[i] means buy after cooldown.
        '''
        if len(prices) < 2:
            return 0
        T = [[0] * 2 for _ in range(len(prices))]
        T[0][1] = -prices[0]
        for i in range(1, len(prices)):
            T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i])
            if i >= 2:
                T[i][1] = max(T[i-1][1], T[i-2][0] - prices[i])
            else:
                T[i][1] = max(T[i-1][1], -prices[i])
        return T[-1][0]