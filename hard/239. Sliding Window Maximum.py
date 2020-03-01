# 239. Sliding Window Maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Use a queue to store the index, and trim its left and right in every iteration to
        remove the impossible index. Then the queue head is the index of the current max.

        Use a deque to store the INDEX, because we need to track what element is expired.
        Before adding the index, do below 3 ops:
        1. remove last added numbers that are smaller than the adding number; Use pop()
        2. remove numbers that are out of window, based on the index; Use popleft()
        3. the leftmost one in the deque will be the max in the sliding window.
           Note that we only start adding element once we see the first complete window.
        """
        ans = []
        q = collections.deque()
        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)
            if i - k >= q[0]:
                q.popleft()
            if i + 1 >= k:
                ans.append(nums[q[0]])
        return ans