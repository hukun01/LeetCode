class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
        q = collections.deque()
        for i, n in enumerate(nums):
            # Before adding new number, remove existing numbers that are smaller than it, 
            # because they are impossible to be the max after adding this new number.
            while q and nums[q[-1]] < n:
                q.pop()
            if q and i - k >= q[0]:
                q.popleft()
            q.append(i)
            if i + 1 >= k:
                ans.append(nums[q[0]])
        return ans