# 810. Chalkboard XOR Game
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        '''
        Say the XOR of all elements is N, erasing an elmenet x updates N to
        (N ^ x), and Alice wants (N ^ x) to not be 0, so she should always
        erase the x that's not equal to N.
        Alice will win when she starts her move if:
        1. the initial N is 0; Or,
        2. the initial N is not 0, not all the elements are the same.
        Alice can always erase a good element (good means that it's not equal
        to the latest N) in this situation. However, to win, the total number
        of elements must starts even. Because Alice needs to let Bob erase from
        an odd-length array full of identical elements, so Bob's move will lead
        N to 0. If the array starts with odd length, Bob would just do the same
        moves to Alice and Alice will lose.
        '''
        N = 0
        for n in nums:
            N ^= n
        return N == 0 or len(nums) % 2 == 0