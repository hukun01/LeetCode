# 260. Single Number III
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        Bit manipulation.
        Find the xor 'xor' of all numbers.
        Find the rightmost 1-bit in (x^y), aka, rightmost 'rightmost_bit' between x and y.
        Iterate through nums, except some number pairs, only one number will
        share the rightmost 1-bit with 'rightmost_bit', xor all such numbers, we will
        get one number x.
        The other number would just be xor ^ x.
        '''
        xor = 0
        for num in nums:
            xor ^= num

        rightmost_bit = xor & (-xor)

        x = 0
        for num in nums:
            if num & rightmost_bit:
                x ^= num

        return [x, xor^x]