# 1567. Maximum Length of Subarray With Positive Product
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        '''
        DP.
        Let f[i] be the [len_of_positive_subarray, len_of_negative_subarray]
        of nums[:i], see below transition functions.
        '''
        f = [[0, 0] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] < 0:
                f[i+1] = [f[i][1] + 1 if f[i][1] > 0 else 0, f[i][0] + 1]
            elif nums[i] > 0:
                f[i+1] = [f[i][0] + 1, f[i][1] + 1 if f[i][1] > 0 else 0]
        return max(x[0] for x in f)
        '''
        Easily O(1) space based on above.
        '''
        f = [0, 0]
        ans = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                f = [f[1] + 1 if f[1] > 0 else 0, f[0] + 1]
            elif nums[i] > 0:
                f = [f[0] + 1, f[1] + 1 if f[1] > 0 else 0]
            else:
                f = [0, 0]
            ans = max(ans, f[0])
        return ans