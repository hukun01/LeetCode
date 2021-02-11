# 204. Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Filtering.
        Have a is_prime array to record whether a number is a prime.
        If a number is not a prime, skip it, otherwise, increment count, and
        mark its multiply as a non prime.

        Time: O(n loglog(n)) see https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes
        Space: O(n)
        '''
        is_prime = [True] * n
        count = 0
        for i in range(2, n):
            if not is_prime[i]:
                continue
            count += 1
            for j in range(i * 2, n, i):
                is_prime[j] = False

        return count