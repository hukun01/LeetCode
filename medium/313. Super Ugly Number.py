# 313. Super Ugly Number
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        Use a heap to store (x, y, i), where x is the x-th
        ugly number, y is the last ugly number that is used
        to multiply with primes[i] to get x.
        In the iteration that runs (n - 1) times, each time
        we multiply primes[i + 1] (a bigger prime) with the
        last ugly number (a smaller ugly number comparing to x).
        And we also multiply primes[i] (a bigger prime) with
        x (a bigger ugly number).
        '''
        k = len(primes)
        q = [(primes[0], 1, 0)]
        x = 1
        for _ in range(n - 1):
            x, y, i = heappop(q)
            
            if i + 1 < k:
                heappush(q, (y * primes[i + 1], y, i + 1))
            
            heappush(q, (x * primes[i], x, i))

        return x