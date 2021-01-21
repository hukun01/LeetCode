# 313. Super Ugly Number
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        Heap.
        We want to generate a series of ugly numbers in acending order. This
        is similar to merge k lists, where we multiple each prime with the
        existing ugly numbers, and append the smallest ugly number to array.

        Use a heap to store (x, p, i), where x is the x-th ugly number, p is
        the prime number used to multiply with ugly[i] to get x.

        Note that we may have duplicate ugly numbers, need to skip them and
        add their next ugly numbers.

        Time: O(n log(k)) where k is len(primes)
        Space: O(n) for storing 'ugly' array.
        '''
        ugly = [1]
        # (ugly number, prime, index to use in 'ugly' for the next entry)
        cand = [(p, p, 0) for p in primes]
        for _ in range(n - 1):
            ugly.append(cand[0][0])
            while cand[0][0] == ugly[-1]:
                x, p, i = heapq.heappop(cand)
                heapq.heappush(cand, (p * ugly[i + 1], p, i + 1))

        return ugly[-1]