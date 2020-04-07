# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        1/2 Binary search, a strange one.

        LIS_list: in this list, index is length of LIS, value is
        the smallest ending number of this LIS with the length.
        '''
        lisList = []
        for x in nums:
            lisLen = bisect.bisect_left(lisList, x)
            if lisLen == len(lisList):
                lisList.append(x)
            else:
                lisList[lisLen] = x
        return len(lisList)
        '''
        2/2 DP

        dp[i] denotes the length of subsequence that ends at i-th element,
        dp[i] = dp[j] + 1 for all j that nums[j] < nums[i].
        The answer is max(dp)
        '''
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0