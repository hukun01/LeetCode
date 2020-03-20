class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        f[i][0] = max(f[i-1][0] * nums[i], f[i-1][1] * nums[i], nums[i]) max positive
        f[i][1] = min(f[i-1][1] * nums[i], f[i-1][0] * nums[i], nums[i]) min negative
        '''
        f = [[0] * 2 for _ in range(2)]
        f[0] = [nums[0], nums[0]]
        ans = nums[0]
        for i in range(1, len(nums)):
            curr = i % 2
            prev = 1 - curr
            candidates = [f[prev][0] * nums[i], f[prev][1] * nums[i], nums[i]]
            f[curr][0] = max(candidates)
            f[curr][1] = min(candidates)
            ans = max(ans, max(f[curr]))
        return ans