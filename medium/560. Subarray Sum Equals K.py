class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Prefix sums.
        Similar to #930

        We are looking for intervals [i:j], where sum[i:j] = k, we know that
        prefixSum[i] = A[0] + ... + A[i],
        so sum[i:j] = prefixSum[j] - prefixSum[i - 1].
        Then we need to find prefixSum[j] - prefixSum[i - 1] = k, which is
        similar to Two Sum.
        One edge case is that current prefixSum = S, when the interval starts
        from the beginning.
        '''
        sumCounter = Counter()
        preSum = ans = 0
        for a in nums:
            sumCounter[preSum] += 1 # the first iteration covers the no-interval edge case
            preSum += a
            ans += sumCounter[preSum - k]
        return ans