# 260. Single Number III
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        Bit manipulation.
        Find the xor 'bitmask' of all numbers.
        Find the rightmost 1-bit in (x^y), aka, rightmost diff between x and y.
        Iterate through nums, except some number pairs, only one number will
        share the rightmost 1-bit with diff, xor all such numbers, we will
        get one number x.
        The other number would just be bitmask ^ x.
        '''
        bitmask = 0
        for num in nums:
            bitmask ^= num

        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask^x]