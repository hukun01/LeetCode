# 991. Broken Calculator
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        '''
        Greedy.
        When X > Y, it's clear that the answer is to subtract (X - Y) times.
        When X < Y, if we try changing X to be greater than Y, there will be
        many cases. However, if we try changing Y to be less than X, there are
        only 2 cases:
        1. Y is even, say 2m, from X to Y, the previous Y' can have 2 values:
           a. Y' = Y / 2 = 2m / 2 = m
           b. Y' = Y + 1 = 2m + 1
           We would never come from #b, because coming from #b means the
           *previous previous value* would be 2m+2, and we have below
           min transition sequence.
           x ... m+1 -> 2(m+1)=2m+2 -> 2m + 1 = Y' -> 2m = Y
           Here from 'm+1', we did 1 multiply, 2 decrement, 3 operations.
           And we can find a shorter path as below.
           x ... m+1 -> m+1-1 = m = Y' -> 2m = Y
           Here from 'm+1', we did 1 decrement, 1 multiply, 2 operations.
           Hence, we always go #a.
        2. Y is odd, meaning the last value Y' must be Y+1.

        Time: O(log Y)
        Space: O(1)
        '''
        ans = 0
        while Y > X:
            ans += 1
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2

        return ans + X - Y