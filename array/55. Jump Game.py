# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Keep track of the current furthest jumpable distance,
        if it's always that furthest >= i for all i, then we can jump.
        '''
        furthest = 0
        for i, n in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i + n)
        return True