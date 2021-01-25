# 1735. Count Ways to Make Array With Product
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        '''
        Math.
        Fundamental theorem of arithmetic - every integer greater than 1 is
        either a prime number or the product of an unique set of prime numbers.
        Mathematically, i = p1^c1 + p2^c2 + .. for any i > 1.

        Based on this theorem, for each query, we can find out the primes that
        form the product k. For a prime factor p1, there are c1 such p1, to be
        placed into n bin, allowing duplication.
        Based on *stars and bars* method in combinatorics, the number of ways
        to place c1 indistinguishable element into n distinguishable slots, is
        comb(c1 + n - 1, c1). This means there are (c1 + n - 1) positions, in
        which there are c1 stars, (n - 1) bars to separate the stars into n
        bins, we can either choose to place c1 stars, or (n - 1) bars into
        these positions.

        Note that after trying placing prime factors for k, if at the end, we
        still have k > 1, that means k is can't be further factorized, we need
        to place k into any of the n slots. Thus, do ways *= n.

        Time: O(Q log(k)) where Q is len(queries)
        Space: O(Q)
        '''
        def get_primes(n):
            primes = []
            for i in range(2, n):
                for j in range(2, i):
                    if i % j == 0:
                        break
                primes.append(i)
            return primes

        primes = get_primes(100)
        ans = []
        MOD = 10 ** 9 + 7
        for n, k in queries:
            ways = 1
            for p in primes:
                if p > k:
                    break
                count = 0
                while k % p == 0:
                    count += 1
                    k //= p
                ways *= comb(n - 1 + count, count)
            if k > 1:
                ways *= n
            ans.append(ways % MOD)

        return ans