# 309. Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        DP.

        Let f[i][0] be the answer for the first i days with no stock at hand.
        Let f[i][1] be the answer for the first i days with a stock at hand.
        f[0] = [0, -inf]
            means to have a stock at hand with no trade, it takes 'inf' cost.
        f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i-1])
            f[i-1][0] means rest from last day; f[i-1][1] + prices[i-1] means
            sell last stock.
        f[i][1] = max(f[i-1][1], f[i-2][0] - prices[i-1])
            f[i-1][1] means rest from last day; f[i-2][0] - prices[i-1] means
            buy after cooldown. Note that it's f[i-2] not f[i-1].

        Time: O(n)
        Space: O(n) can be reduced to O(1)

        Another great post that explains all: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        '''
        n = len(prices)
        if n < 2:
            return 0

        f = [[0, 0] for _ in range(n + 1)]
        f[0] = [0, -inf]
        for i in range(1, n + 1):
            f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i-1])
            f[i][1] = max(f[i-1][1], f[i-2][0] - prices[i-1])

        return f[-1][0]