# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        1/2 Binary search, a strange one.
        
        Keep a tails array that records the smallest element in the target subsequence.
        When we see a new n, if tails[i] < n <= tails[j], then replace tails[j] = n;
        if n > tails[j], then append n to tails.
        This way we keep the invariance that tails is increasing. Hence the result is len(tails)
        '''
        tails = []
        for n in nums:
            i, j = 0, len(tails)
            while i < j:
                m = (i + j) // 2
                if n <= tails[m]:
                    j = m
                else:
                    i = m + 1
            if i == len(tails):
                tails.append(n)
            else:
                tails[i] = n
        return len(tails)
        '''
        2/2 DP

        dp[i] denotes the length of subsequence that ends at i-th element,
        dp[i] = dp[j] + 1 for all j that nums[j] < nums[i].
        The answer is max(dp)


        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0
        '''