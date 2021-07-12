# 123. Best Time to Buy and Sell Stock III
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        DP.
        T[i][k][0] is the max profit with 0 stock left after i-th day with k transaction
        T[i][k][1] is the max profit with 1 stock left after i-th day with k transaction
        i is in [1, len(prices)], k is in [1, 2]
        T[0][1][1] = T[0][2][1] = -math.inf
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
        Note that one transaction consists of buy and sell, here we only increment k
        when buying.
        '''
        n = len(prices)
        T = [[[0] * 2 for k in range(3)] for i in range(n + 1)]
        T[0][1][1] = T[0][2][1] = -inf
        for i in range(1, n + 1):
            for k in range(1, 3):
                T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i-1])
                T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i-1])
        return T[-1][-1][0]
        '''
        Improvements:
        Since T[i][k] depends on T[i-1][k] and T[i-1][k-1], we can convert 
        the O(kn) space into O(k) space. In this case it would be O(1) space.
        '''
        Ti10 = Ti20 = 0
        Ti11 = Ti21 = -math.inf
        for p in prices:
            Ti10 = max(Ti10, Ti11 + p)
            Ti11 = max(Ti11, -p)
            Ti20 = max(Ti20, Ti21 + p)
            Ti21 = max(Ti21, Ti10 - p)
        return Ti20