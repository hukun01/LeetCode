# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        1/2 Binary search and DP.

        LIS_list: in this list, index is length of LIS, value is
        the smallest ending number of this LIS with the length.
        Time: O(nlog(n)) where n is len(nums).
        Space: O(n)
        '''
        lisList = []
        for x in nums:
            lisLen = bisect_left(lisList, x)
            if lisLen == len(lisList):
                lisList.append(x)
            else:
                lisList[lisLen] = x
        return len(lisList)
        '''
        1.5/2 A more compact version based on 1/2.
        We can pre-fill inf to the lens array, so we wouldn't need to check
        whether the current element is the largest, but just replace with it.
        Time and Space: same as above.
        '''
        lens = [inf] * len(nums)
        for a in nums:
            lens[bisect_left(lens, a)] = a
        return bisect_left(lens, inf)
        '''
        2/2 DP

        dp[i] denotes the length of subsequence that ends at i-th element,
        dp[i] = dp[j] + 1 for all j that nums[j] < nums[i].
        The answer is max(dp).
        Time: O(n^2)
        Space: O(n)
        '''
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0