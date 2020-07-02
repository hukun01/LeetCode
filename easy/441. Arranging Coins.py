# 441. Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        Middle school math.
        Assume the answer is x, then n >= x(1 + x) / 2,
        so x(1 + x) <= 2n.
        Transform this into (x + 1/2)^2 - 1/4 <= 2n, then
        x <= sqrt(2n + 1/4) - 1/2.
        '''
        return int((2 * n + 0.25) ** 0.5 - 0.5)