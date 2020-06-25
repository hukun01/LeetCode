class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Similar to 3Sum, where we need to sort the nums.
        '''
        nums.sort()
        ans = sum(nums[0:3])
        for left in range(len(nums)-2):
            if left > 0 and nums[left-1] == nums[left]:
                continue
            middle, right = left + 1, len(nums) - 1
            while middle < right and ans != target:
                curr_sum = nums[left] + nums[middle] + nums[right]
                ans = min(ans, curr_sum, key=lambda x: abs(x - target))
                if curr_sum < target:
                    middle += 1
                else:
                    right -= 1
                
        return ans