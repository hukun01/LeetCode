# 717. 1-bit and 2-bit Characters
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        '''
        Check the bit from the end, if there's odd number of *consecutive* 1s,
        the last character must not be a one-bit character, because
        all other 1s would be '11' except for one 1 that would use '10'.
        '''
        ones = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] != 1:
                break
            ones += 1
        return ones % 2 == 0