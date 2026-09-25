# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Same as the 746. Min Cost Climbing Stairs, just without cost.
        'a' denotes the #ways to reach the (i-2)th stair;
        'b' denotes the #ways to reach the (i-1)th stair.

        Reaching the (i)th stair can be done by
        1. taking 1 step from (i-1)th stair;
        2. taking 2 steps from (i-2)th stair.
        So let 'c' denote the #ways to reach the (i)th stair, c = a + b.
        Then we roll forward, 'a' moves from (i-2)th to (i-1)th, aka, a = b.
        Similarly b = c.
        '''
        a = b = 1
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b
