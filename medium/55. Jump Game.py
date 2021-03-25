# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Record the current furthest reachable position and the current
        position, and the index in nums.
        Within the furthest reachable position, we pick the next furthest
        position. If the next one cannot exceed the current furthest, we can't
        proceed.

        Time: O(n)
        Space: O(1)
        '''
        n = len(nums)
        furthest = 0
        i = 0
        while furthest < n - 1:
            next_furthest = furthest
            while i <= furthest:
                next_furthest = max(next_furthest, i + nums[i])
                i += 1

            if furthest == next_furthest:
                break

            furthest = next_furthest

        return furthest >= n - 1