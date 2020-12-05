# 1492. The kth Factor of n
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        '''
        Math.
        The factors appear in pairs, f1 * f2 = n.
        Assume f1 <= f2, we know that all f1 <= sqrt(n).
        We try every number from [1, sqrt(n)] inclusive, and decrement k.
        If k becomes 0, we return the current f1; Otherwise, we find its f2,
        which is n // f1s[-k].
        One exception is that n is a square number, in which we track an extra
        pair where f1 = f2 = sqrt(n), in this case we increment k by 1 to skip
        this f2 that doesn't really exist.

        Time: O(sqrt(n))
        Space: O(sqrt(n))
        '''
        divisors = []
        n_sqrt = int(n ** 0.5)
        for i in range(1, n_sqrt + 1):
            if n % i != 0:
                continue
            k -= 1
            divisors.append(i)
            if k == 0:
                return i
        if n_sqrt ** 2 == n:
            k += 1
        return n // divisors[-k] if k <= len(divisors) else -1