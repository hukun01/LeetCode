# 154. Find Minimum in Rotated Sorted Array II
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Binary search.
        A key is that when nums[m] == nums[h], we don't know which side
        the min could be in, so have to do a linear scan.
        '''
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            elif nums[m] < nums[h]:
                h = m
            else:
                h -= 1

        return nums[l]