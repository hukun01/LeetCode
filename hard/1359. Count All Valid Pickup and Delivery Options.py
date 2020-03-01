# 1359. Count All Valid Pickup and Delivery Options
class Solution:
    def countOrders(self, n: int) -> int:
        '''
        Assume we already have (i-1) pairs, and we are going to insert
        the i-th pair.
        To insert the first element, there are (2i - 2 + 1) slots;
        After that, to insert the second element, there are (2i) slots.
        Because first element must stay first, the number of pair permutations
        needs to be divided by 2.
        To start, for the first pair, we only have one choice.
        '''
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(2, n + 1):
            ans = ans * (i * 2 - 1) * (i * 2) // 2 % MOD
        return ans