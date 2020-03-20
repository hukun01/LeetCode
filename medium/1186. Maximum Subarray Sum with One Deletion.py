# 1186. Maximum Subarray Sum with One Deletion
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        '''
        dp[i][0] tracks the max sum without skipping anything, 
        dp[i][1] tracks the max sum with skipping some negative element.
        
        dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i], arr[i])
        '''
        if len(arr) == 1:
            return arr[0]
        dp = [[0] * 2 for _ in range(2)]
        dp[0] = [arr[0], 0]
        ans = -float('inf')
        for i in range(1, len(arr)):
            curr = i % 2
            prev = (i - 1) % 2
            dp[curr][0] = max(arr[i], dp[prev][0] + arr[i])
            dp[curr][1] = max(dp[prev][0], dp[prev][1] + arr[i], arr[i])
            ans = max(ans, max(dp[curr]))
        return ans