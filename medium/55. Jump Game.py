# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Keep track of the current furthest jumpable distance,
        if it's always that furthest >= i for all i, then we can jump.
        In another word, if any position > furthest, we can't jump to it.
        '''
        furthest = 0
        for i, n in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i + n)
        return True