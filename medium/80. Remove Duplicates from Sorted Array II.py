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
'''
Another more generic approach that can handle any number of allowed duplicates.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            counter = 0
            while j + counter < len(nums) and nums[j + counter] == nums[j]:
                if counter < 2:
                    nums[i] = nums[j]
                    i += 1
                counter += 1
            
            j += counter
            
        return i
