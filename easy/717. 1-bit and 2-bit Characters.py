# 717. 1-bit and 2-bit Characters
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        '''
        Check the bit from the end, if there's odd number of *consecutive* 1s,
        the last character must not be a one-bit character, because
        all other 1s would be '11' except for one 1 that would use '10'.
        '''
        n = len(bits)
        if n == 1:
            return True
        ones = 0
        for i in range(n - 2, -1, -1):
            if bits[i] == 1:
                ones += 1
            else:
                break
        return ones % 2 == 0