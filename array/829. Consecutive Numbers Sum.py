class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        We are looking for below sequence
        N = x + (x+1) + (x+2) + ... + (x+k-1)
          = kx + (1 + 2 + .. + k - 1)
          = kx + (k-1)(1 + k - 1) / 2
          = kx + k(k-1)/2
        Basically we are looking for kx (or a number that % k == 0),
        and kx = N - k(k-1)/2
        we know kx > 0, so N > k(k-1)/2 which is 2N > k(k-1), and it
        can be approximated to 2N > (k-1)(k-1), which is k < sqrt(2N) + 1

        Note that we should start k from 2 to ensure the consecutive arrays
        have at least 2 numbers (see the initial equation x + ..+(x + k - 1)).
        '''
        count = 1
        for k in range(2, int((2*N)**(0.5)) + 1):
            if (N - (k * (k - 1) // 2)) % k == 0:
                count += 1
        return count