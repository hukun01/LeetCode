# 260. Single Number III
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        Bit manipulation.
        Let a, b be these two one-time elements. Let 'xor' be the xor of all
        numbers, we have xor = (a^b).
        Find the lowest 1-bit in 'xor' by 'xor & -xor', this is also the
        tehcnique used in Binary Indexed Tree. This is the bit where a and b
        differs.
        Iterate through nums, except some number pairs, only one number will
        also have this lowest bit set, so xor all such numbers, we will get
        number 'a'
        The other number would just be xor ^ a.

        Time: O(n) where n is len(nums)
        Space: O(1)
        '''
        xor = reduce(lambda a, b: a ^ b, nums)

        lowest_bit = xor & (-xor)

        a = 0
        for num in nums:
            if num & lowest_bit:
                a ^= num

        return [a, xor^a]