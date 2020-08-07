# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        1/2 Binary search
        '''
        l, h = min(nums), max(nums)
        k -= 1
        while l < h:
            m = (l + h) // 2
            greater_than_m = sum(n > m for n in nums)
            if greater_than_m <= k:
                h = m
            else:
                l = m + 1
        return l
        '''
        2/2 Quick select
        Standard quick select algorithm, similar to 973. K Closest Points to Origin.
        '''
        def sort(start, end):
            while start != end:
                pivot_idx = partition(start, end)
                if len(nums) - k == pivot_idx:
                    return nums[pivot_idx]
                elif pivot_idx > len(nums) - k:
                    end = pivot_idx - 1
                else:
                    start = pivot_idx + 1
            return nums[start]
        
        def partition(start, end):
            pivot_idx = random.randint(start, end)
            pivot = nums[pivot_idx]
            nums[end], nums[pivot_idx] = nums[pivot_idx], nums[end]
            stored_idx = start
            for i in range(start, end): # excluding end
                if nums[i] < pivot:
                    nums[stored_idx], nums[i] = nums[i], nums[stored_idx]
                    stored_idx += 1
            nums[end], nums[stored_idx] = nums[stored_idx], nums[end]

            return stored_idx # do NOT return pivot_idx!
        
        return sort(0, len(nums) - 1)