class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Similar to 3Sum, where we need to sort the nums.
        '''
        nums.sort()
        ans = sum(nums[:3])
        n = len(nums)
        for left in range(n-2):
            if left > 0 and nums[left-1] == nums[left]:
                continue
            mid = left + 1
            right = n - 1
            while mid < right and ans != target:
                cur = nums[left] + nums[mid] + nums[right]
                ans = min(ans, cur, key=lambda x: abs(x - target))
                if cur < target:
                    mid += 1
                else:
                    right -= 1

        return ans