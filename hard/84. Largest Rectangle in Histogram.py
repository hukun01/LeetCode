# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Mono stack.
        A rectangle is formed by a width and a height, the height must be the
        shortest one within that width.
        When scanning through the heights,
            when we see a lower height, we have to use it, because the
            previous higher heights can't be used.
            when we see a higher height, we don't have to use it now, because
            in the future we may get more higher heights that would be
            constrained by our previous lower height just like the current
            higher height.
        Thus, we maintain a monotonically increasing stack. When we see a
        higher height, we just push into the stack.
        When we see a lower height, we start using the higher heights in the
        stack by poping them out. Within the current heights, we can find a
        rectangle that uses a higher height than the current height. When we
        do this, we also record the previous index of the higher heights, but
        replace it with the current height, as that's the best we can get after
        the current height.
        We add a 0 to the end of heights so that we use the same logic to
        process the tail of the sequence that can be monotonically increasing.

        Time: O(n) where n is len(heights)
        Space: O(n)
        '''
        left = []
        maxArea = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while left and h <= left[-1][0]:
                prevH, prevStart = left.pop()
                maxArea = max(maxArea, (i - prevStart) * prevH)
                start = prevStart
            left.append((h, start))
        return maxArea