# 1808. Maximize Number of Nice Divisors
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        '''
        Math.
        Represent n as p1^a1 * p2^a2...*px^ax, where p1,p2,px are prime
        factors, a1,a2,ax are the power. A nice divisor takes at least one from
        each of the a1,a2,ax.
        Then the goal is to find the max combinations from a1,a2,ax, which is
        a1 * a2 * ax, and satisfy that a1 + a2 + ... + ax <= primeFactors.

        Now this is identical to 343. Integer Break, except we also need to do
        mod operations.

        Time: O(log(n))
        Space: O(1)
        '''
        if primeFactors <= 3:
            return primeFactors
        MOD = 10 ** 9 + 7
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, MOD)
        elif primeFactors % 3 == 1:
            return 4 * pow(3, (primeFactors - 4) // 3, MOD) % MOD
        else:
            return 2 * pow(3, (primeFactors - 2) // 3, MOD) % MOD