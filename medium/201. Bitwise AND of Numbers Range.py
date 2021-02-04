# 201. Bitwise AND of Numbers Range
class Solution:
    def rangeBitwiseAnd(self, s: int, e: int) -> int:
        '''
        Bit manipulation.

        See an example below,
        0101 = 5
        0110 = 6
        0111 = 7
        --------
        0100 = 4

        In this example, we keep counting the length of lower mismatch bits
        between the two numbers, and also shift them to the right. If two
        numbers mismatch, their difference is at least 1, then one of the
        lowest bit would be different than the other, so mismatch means 0.

        Once two numbers become equal, they share all higher bits. Now we can
        shift s back to the left, by 'mismatch' positions, effectively filling
        lower bits with 0.

        Time: O(1)
        Space: O(1)
        '''
        mismatch = 0
        while s != e:
            s >>= 1
            e >>= 1
            mismatch += 1
        return s << mismatch