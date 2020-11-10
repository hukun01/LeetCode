# 188. Best Time to Buy and Sell Stock IV
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        DP.
        Let f[i][0][k] be the max profit with first i prices, k transactions,
        and have stock at hand.
        Let f[i][1][k] be the similar, but have no stock at hand.

        f[i][0][k] = max(f[i-1][0][k], f[i][1][k-1] - p)
        f[i][1][k] = max(f[i-1][1][k], f[i][0][k] + p)

        f[0][0] = [-math.inf] * (k+1)
        ans = max(f[i][1])

        The key is to only increase the transactions count when buying.
        Time is O(nk) if k < n//2, otherwise O(n).
        Space is O(nk).
        '''
        n = len(prices)
        if k >= n//2:
            # There's no practical limit as k is big.
            return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)

        f = [[[0] * (k + 1) for hand in range(2)] for _ in range(n + 1)]
        f[0][0] = [-math.inf] * (k + 1)
        for i in range(1, n+1):
            p = prices[i-1]
            for k_i in range(1, k+1):
                f[i][0][k_i] = max(f[i-1][0][k_i], f[i][1][k_i-1] - p)
                f[i][1][k_i] = max(f[i-1][1][k_i], f[i][0][k_i] + p)
        return max(f[n][1])
        '''
        Space optimized DP.
        Notice that in the above DP transition functions, f[i] only depends on
        f[i-1] and itself, so we can use rolling arrays. Space is O(k).
        '''
        n = len(prices)
        if k >= n//2:
            return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)
        f0 = [[0] * (k + 1) for hand in range(2)]
        f0[0] = [-math.inf] * (k + 1)
        for i in range(1, n+1):
            p = prices[i-1]
            fi = [[0] * (k + 1) for hand in range(2)]
            for k_i in range(1, k+1):
                fi[0][k_i] = max(f0[0][k_i], fi[1][k_i-1] - p)
                fi[1][k_i] = max(f0[1][k_i], fi[0][k_i] + p)
            f0 = fi
        return max(f0[1])