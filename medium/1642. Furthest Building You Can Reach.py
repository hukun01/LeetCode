# 1642. Furthest Building You Can Reach
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        Heap.
        Use ladders for the largest height diffs, use bricks for the rest.
        Use a heap to store the k largest height diffs, where k == len(ladders).
        Every time we get more than k heigh diffs, pop out the smallest diff,
        and replace that ladder with bricks. Whenever we run out of bricks, we
        have already made the most out of the ladders.

        Time: O(n log(L)) where n is len(heights), L is ladders.
        Space: O(L)

        The idea behind replacing ladder with bricks is similar to that in the
        630. Course Schedule III where we replace a longer course with a
        shorter one, and keep the current time before deadline.
        '''
        heap = []
        n = len(heights)
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heappop(heap)
            if bricks < 0:
                return i
        return n - 1