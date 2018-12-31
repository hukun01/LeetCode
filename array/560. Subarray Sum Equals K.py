class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        Similar to #930
        
        We are looking for intervals [i:j], where sum[i:j] = k, we know that
        prefixSum[i] = A[0] + ... + A[i], so sum[i:j] = prefixSum[j] - prefixSum[i - 1].
        Then we need to find prefixSum[j] - prefixSum[i - 1] = k, which is similar to 2Sum.
        One edge case is that current prefixSum = S, when the interval starts from the beginning.
        """
        c = collections.Counter()
        preSum = ans = 0
        for a in nums:
            c[preSum] += 1 # the first iteration covers the no-interval edge case
            preSum += a
            ans += c[preSum - k]
        return ans