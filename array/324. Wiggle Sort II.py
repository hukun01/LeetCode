# 324. Wiggle Sort II
import statistics
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1/2 Simple solution using sorting with O(NlogN) time.
        Sort and find the median, and slice the list such that we
        assign numbers smaller than mid to odd slots, and bigger numbers
        to even slots.
        
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2],nums[0::2] = nums[:mid], nums[mid:]
        '''

        '''
        2/2 Complex soultion but using O(N) time and O(1) space

        Find the median using "statistics.median(list)", this should be O(N).

        Do a 3-way-partitioning, or color sort, we can sort the nums
        into 3 parts [smallers, medians, biggers]
        When doing the color sort:
            For smallers, remap the index to odd slots;
            For biggers, remap the index to even slots.
            For medians, keep them unchanged.
        The remap logic relies on the relative position of the index,
        when the index falls into the first half of the list, it maps to
        odd slots, when it falls into the second half, it maps to even slots.

        In the classic color sort:
        [ :i] are values less than mid;
        [i:j] are values equal to mid;
        [j:k] are values not yet sorted;
        [k: ] are values greater than mid
        '''
        def remap(i):
            return (1 + 2 * i) % (len(nums) | 1)
        def swapRemap(a, b):
            nums[remap(a)], nums[remap(b)] = nums[remap(b)], nums[remap(a)]
        i = j = 0
        k = len(nums) - 1
        mid = statistics.median(nums)
        while j <= k:
            if nums[remap(j)] < mid:
                swapRemap(j, k)
                k -= 1
            elif nums[remap(j)] > mid:
                swapRemap(i, j)
                i += 1
                j += 1
            else:
                j += 1