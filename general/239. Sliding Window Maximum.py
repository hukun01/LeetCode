class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Use a deque to store the INDEX, because we need to track what element is expired.
        Before adding the index, do below 3 ops:
        1. remove numbers that are out of window, based on the index; Use popleft()
        2. remove last added numbers that are smaller than the adding number; Use pop()
        3. the leftmost one in the deque will be the max in the sliding window.
        """
        ans = []
        queue = collections.deque()
        for i in range(len(nums)):
            # Before adding new number, remove existing numbers that are smaller than it, 
            # because they are impossible to be the max after adding this new number.
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
            if queue and i - queue[0] >= k - 1:
                queue.popleft()
        return ans