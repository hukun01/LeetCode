class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        A rectangle is formed by a width and a height, the height must be the shortest one within that width.
        When scanning through the heights,
            when we see a lower height, we have to use it, because the previous higher heights can't be used.
            when we see a higher height, we don't have to use it now, because in the future we may get more higher
            heights that would be constrained by our previous lower height just like the current higher height.
        Thus, we maintain a monotonically increasing stack. When we see a higher height, we just push into the stack.
        When we see a lower height, we start using the higher heights in the stack by poping them out. Within the
        current heights, we can find a rectangle that uses a higher height than the current height. When we do this,
        we implicitly replace those higher heights with our current height, that's the best we can get after the current
        height.
        We add a 0 to the end of heights so that we use the same logic to process the tail of the sequence that can be
        monotonically increasing.
        '''
        left = []
        maxArea = 0
        heights += [0]
        for i, h in enumerate(heights):
            start = i
            while left and left[-1][0] >= h:
                prevH, prevStart = left.pop()
                maxArea = max(maxArea, (i - prevStart) * prevH)
                start = prevStart
            left.append((h, start))
        return maxArea