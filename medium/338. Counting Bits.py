# 338. Counting Bits
class Solution:
    def countBits(self, num: int) -> List[int]:
        '''
        If i is even, then in binary we just left shift (i // 2), so
        the number of 1 bits is the same; if i is odd, in binary we
        just flip the last digit of (i - 1), so it's (ans[i - 1] + 1)
        '''
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0:
                ans[i] = ans[i // 2]
            else:
                ans[i] = ans[i - 1] + 1
        return ans