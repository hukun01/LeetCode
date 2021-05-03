# 1798. Maximum Number of Consecutive Values You Can Make
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        '''
        Sort + accumulate.
        A number can only be made by the smaller numbers, so we sort coins.
        Let 'cur' be the number we are trying to make, and we already made
        a consecutive internval [0, cur-1]. Iterate through the coins from
        small to large values, for each coin c, if we add c to cur, that means
        we can make a consecutive interval [c, cur+c-1], and if c <= cur, then
        we can make a consecutive interval [0, cur+c-1]. Otherwise, if c > cur,
        the [0, cur+c-1] can't be consecutive, and 'cur' is the first number we
        can't make.

        Time: O(n log(n)) where n is len(coins)
        Space: O(n)
        '''
        cur = 1
        for c in sorted(coins):
            if c <= cur:
                cur += c
            else:
                break

        return cur