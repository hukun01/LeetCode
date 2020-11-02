# 673. Number of Longest Increasing Subsequence
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        Similar to 300. Longest Increasing Subsequence.
        LIS_list: in this list, index is length of LIS, value is
        the smallest ending number of this LIS with the length.

        Let dp[k][x] be the number of LIS with length k that ends with number x.
        dp[k][x] = sum of dp[k-1][y] for y < x.
        '''
        if not nums:
            return 0
        dp = defaultdict(Counter)
        dp[0][-math.inf] = 1

        # LIS_list: index is length of LIS, value is
        # the smallest ending number with that length.
        lisList = []
        for x in nums:
            lisLen = bisect.bisect_left(lisList, x)
            if lisLen == len(lisList):
                lisList.append(x)
            else:
                lisList[lisLen] = x 
            dp[lisLen+1][x] += sum(count for y, count in dp[lisLen].items() if y < x)
        return sum(dp[len(lisList)].values())