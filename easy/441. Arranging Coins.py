# 441. Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        Middle school math.
        Assume the answer is x, we have below
        n >= 1 + 2 + ... + x = x * (1 + x) / 2 > x * x / 2
        x < sqrt(2n)
        int(sqrt(2n)) is in [x, x + 1]
        Now just need to ensure my sqrt is not too big.
        '''
        my_sqrt = int((2 * n) ** 0.5)
        if my_sqrt * (1 + my_sqrt) // 2 > n:
            my_sqrt -= 1
        return my_sqrt