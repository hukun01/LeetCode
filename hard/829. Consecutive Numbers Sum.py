# 829. Consecutive Numbers Sum
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        Math.
        We are looking for below sequence
        N = x + (x+1) + (x+2) + ... + (x+k-1)
          = kx + (1 + 2 + .. + k - 1)
          = kx + (k-1)(1 + k - 1) / 2
          = kx + k(k-1)/2

        Hence kx = N - k(k-1)/2, we want to find the number of different 'x'.
        Namely, we find the # of cases such that (N - k(k-1)/2) % k == 0.

        Note that we should start k from 2 to ensure the consecutive arrays
        have at least 2 numbers (see the initial equation x + ..+(x + k - 1)).        
        So we have:
        k >= 2, x > 0
        So kx = N - k(k-1)/2 > 0, or N > k(k-1)/2 > (k-1)(k-1)/2, which is
        k < sqrt(2N) + 1
        We try all the possible 'k' and increment count whenever it satisfies
        the above case.

        Time: O(sqrt(N))
        Space: O(1)
        '''
        count = 1
        for k in range(2, int((2*N)**(0.5)) + 1):
            if (N - (k * (k - 1) // 2)) % k == 0:
                count += 1
        return count