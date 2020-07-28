# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Key is to be concise.
        '''
        i = 0
        for a in nums:
            if i < 2 or a > nums[i-2]:
                nums[i] = a
                i += 1
        return i