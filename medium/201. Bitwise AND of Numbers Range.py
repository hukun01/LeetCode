# 201. Bitwise AND of Numbers Range
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        '''
        Number n will have i-th bit if (1 << i) <= n < (1 << (i + 1)),
        A range [m, n] will have i-th bit if (1 << i) <= m and n < (1 << (i + 1)).
        '''
        i = len(bin(m)) - 3
        ans = 0
        while i >= 0:
            x = (1 << i)
            if x <= m and n < (x << 1):
                ans |= (1 << i)
                m -= x
                n -= x
            i -= 1
        return ans