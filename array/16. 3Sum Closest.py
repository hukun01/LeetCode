class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Similar to 3Sum, where we need to sort the nums.
        Note that somehow ans = min(ans, currSum, key=lambda x: abs(x - target)) is really slow.
        '''
        nums.sort()
        ans = sum(nums[0:3])
        for left in range(len(nums)-2):
            if left > 0 and nums[left-1] == nums[left]:
                continue
            middle, right = left + 1, len(nums) - 1
            while middle < right:
                currSum = nums[left] + nums[middle] + nums[right]
                if currSum == target:
                    return currSum
                if currSum < target:
                    middle += 1
                else:
                    right -= 1
                if abs(ans - target) > abs(currSum - target):
                    ans = currSum
        return ans