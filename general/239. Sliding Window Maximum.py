class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Use a deque to store the INDEX!
        Before adding the index, do below 3 ops:
        1. remove numbers that are out of window; Use popleft()
        2. remove last added numbers that are smaller than the latest adding number; Use pop()!
        3. the leftmost one in the deque will be the max in the sliding window.
        """
        deque = collections.deque()
        ans = []
        for i, n in enumerate(nums):
            if deque and i - deque[0] > k - 1:
                deque.popleft()
            # Before adding new number, remove existing numbers that are smaller than it, 
            # because they are impossible to be the max after adding this new number.
            while deque and nums[deque[-1]] < n:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                ans.append(nums[deque[0]])
        return ans