# 84. Largest Rectangle in Histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Monotonic increasing stack.
        A rectangle is formed by a width and a height, the height must be the
        shortest one within that width.
        When scanning through the heights,
            when we see a lower height, we have to use it, because the current
            lower height invalidates the previous heights.
            when we see a higher height, we don't have to use it now, because
            in the future we may get more higher heights that form bigger
            answer. More importantly, our previous heights aren't invalidated.

        Thus, we maintain a monotonically increasing stack. When we see a higher
        height, we just push into the stack.

        When we see a lower height 'h' at index 'i', we start using the
        existing higher heights in the stack and pop them out. Within the
        existing higher heights, we can form a rectangle by a 'prev_h' higher
        than 'h'.
        In the stack, we also record the index 'prev_start' of 'prev_h'.
        'prev_start' is the left index since which 'prev_h' is the lowest
        height. When we pop out stack, we get 'prev_h' and 'prev_start', and
        for each 'h', as we pop out stack, we record the smallest 'prev_start'
        which is the range impacted by 'h', because 'h' is the lowest height
        from 'prev_start' to 'i'.
        Also, in the meantime, a candidate answer is 'prev_h * width' where
        'width = i - prev_start'.

        We add a 0 to the end of heights so that this lowest height triggers
        the same logic to process the tail of the sequence that can be
        monotonically increasing.

        Time: O(n) where n is len(heights)
        Space: O(n)

        PS: monotonic stack is often useful in problems that need local
        min/max, so is the idea in this problem. The lowest histogram can be
        min of subarray in another problem, and the 'area' info can be other
        attributes that are related to subarray min.
        '''
        left = []
        ans = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while left and h <= left[-1][0]:
                prev_h, prev_start = left.pop()
                ans = max(ans, (i - prev_start) * prev_h)
                start = prev_start
            left.append((h, start))

        return ans