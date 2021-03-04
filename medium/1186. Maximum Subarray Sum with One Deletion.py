# 1186. Maximum Subarray Sum with One Deletion
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        '''
        DP.
        Let f[i][0] tracks the max sum with one deletion in nums[:i];
        Let f[i][1] tracks the max sum with no deletion in nums[:i].

        Range for i is [0, n), transition functions as below:
        f[i+1][0] = max(f[i][0] + arr[i], f[i][1])
            This means we either take arr[i] or we don't.

        f[i+1][1] = max(f[i][1], 0) + arr[i]
            This means we either add arr[i] to the previous subarray or start a
            new one.

        Time: O(n)
        Space: O(n) can be reduced to O(1).
        '''
        n = len(arr)
        f = [[-inf, -inf] for _ in range(n+1)]
        ans = -inf
        for i in range(n):
            f[i+1][0] = max(f[i][0] + arr[i], f[i][1])
            f[i+1][1] = max(f[i][1], 0) + arr[i]
            ans = max(ans, *f[i+1])

        return ans