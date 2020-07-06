# 264. Ugly Number II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        Following an ugly number 1, the next ugly number must be min of
        2 * 1, 3 * 1, 5 * 1.
        The key is that we don't want to repeatedly add any ugly number,
        so if 2 * 1 is used, next time we should look at
        2 * 2, 3 * 1, 5 * 1.
        Hence, we keep a separate index for each factor, respectively.
        '''
        ugly = [0] * n
        ugly[0] = 1
        idx2 = idx3 = idx5 = 0
        f2, f3, f5 = 2, 3, 5
        for i in range(1, n):
            ugly[i] = min(f2, f3, f5)
            if f2 == ugly[i]:
                idx2 += 1
                f2 = 2 * ugly[idx2]
            if f3 == ugly[i]:
                idx3 += 1
                f3 = 3 * ugly[idx3]
            if f5 == ugly[i]:
                idx5 += 1
                f5 = 5 * ugly[idx5]
        return ugly[-1]