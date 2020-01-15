# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Standard quick select algorithm, similar to 973. K Closest Points to Origin.
        '''
        def sort(start, end):
            while start != end:
                pivotIdx = partition(start, end)
                if len(nums) - k == pivotIdx:
                    return nums[pivotIdx]
                elif pivotIdx > len(nums) - k:
                    end = pivotIdx - 1
                else:
                    start = pivotIdx + 1
            return nums[start]
        
        def partition(start, end):
            pivotIdx = random.randint(start, end)
            pivot = nums[pivotIdx]
            nums[end], nums[pivotIdx] = nums[pivotIdx], nums[end]
            storedIdx = start
            for i in range(start, end): # excluding end
                if nums[i] < pivot:
                    nums[storedIdx], nums[i] = nums[i], nums[storedIdx]
                    storedIdx += 1
            nums[end], nums[storedIdx] = nums[storedIdx], nums[end]

            return storedIdx # do NOT return pivotIdx!
        
        return sort(0, len(nums) - 1)