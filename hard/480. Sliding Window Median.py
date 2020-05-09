# 480. Sliding Window Median
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        '''
        1/2 Brute force.
        Maintain a window with k sorted numbers, keep removing the leftmost number in nums
        as the window slides to the right.
        
        Time complexity: O(nk)
        Note that these two implementaions have the same time complexities, but in practice,
        the first one is faster.
        1. idx = bisect.insort(list, val) and list.pop(idx)
        2. list.remove(val)
        '''
        window = []
        ans = []
        for i, n in enumerate(nums):
            bisect.insort(window, n)
            if len(window) == k:
                ans.append(window[k//2] if k % 2 == 1 else (window[k//2] + window[(k - 1)//2]) / 2)
                idx = bisect.bisect_left(window, nums[i - k + 1])
                window.pop(idx)
        return ans