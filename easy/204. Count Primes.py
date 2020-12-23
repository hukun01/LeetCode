# 204. Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Filtering.
        Have a not_prime array to record whether a number is a prime.
        If a number is not a prime, skip it, otherwise, increment count, and
        mark its multiply as a non prime.

        Time: O(n loglog(n)) see https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes
        Space: O(n)
        '''
        not_prime = [False] * n
        count = 0
        for i in range(2, n):
            if not not_prime[i]:
                count += 1
                for j in range(i*2, n, i):
                    not_prime[j] = True
        return count