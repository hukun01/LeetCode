# 757. Set Intersection Size At Least Two
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        '''
        Greedy.
        Sort intervals by end time, we focus on checking the rightmost two
        points, because these two points are the last chance to cover the
        current interval.
        Use 'overlapped' to track the current 2 overlapped points.
        If overlapped[1] < start, we need new interval of [e - 1, e] to cover
        the current interval.
        If overlapped[1] >= start and overlapped[0] < start, there's one
        overlapped point, which is overlapped[1], it can be in the middle
        of the current interval, or can be at the end. We need to add another
        overlapped point, if current overlapped is at the end, we add 'end-1';
        if not, we keep overlapped[1] but move it to the first element, and
        hold the second element as 'end'.

        Time: O(n log(n)) where n is len(intervals)
        Space: O(n)
        '''
        ans = 0
        overlapped = []
        for start, end in sorted(intervals, key=lambda i: i[1]):
            if not overlapped or overlapped[1] < start:
                ans += 2
                overlapped = [end - 1, end]
            elif overlapped[0] < start:
                ans += 1
                if overlapped[1] == end:
                    overlapped = [end - 1, end]
                else:
                    overlapped = [overlapped[1], end]

        return ans