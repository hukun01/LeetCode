# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Keep track of the current furthest jumpable distance,
        if it's always that furthest >= i for all i, then we can jump.
        In another word, if any position > furthest, we can't jump to it.
        '''
        furthest = cur = 0
        i = 0
        while furthest < n - 1:
            while i <= cur:
                furthest = max(furthest, i + nums[i])
                i += 1
            if furthest == cur:
                break
            cur = furthest
        return furthest >= n - 1