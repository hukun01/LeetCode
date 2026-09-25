class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        The trick to get the last bit is to do `n & 1`.
        '''
        ans = 0
        shift = 31
        while n:
            lastBit = n & 1
            n = n >> 1
            ans += lastBit << shift
            shift -= 1
            
        return ans
