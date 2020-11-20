# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        Binary Search.
        Similar to 33. Search in Rotated Sorted Array, except that we need
        to handle duplicates by checking nums[l] == nums[m] == nums[h] and
        shrink the search space linearly.
        Time: O(nlog(n)) best case, O(n) worst case.
        Space: O(1).
        '''
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return True

            if nums[l] == nums[m] == nums[h]:
                l += 1
                h -= 1
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        return False