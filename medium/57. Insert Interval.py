# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        1/2 Scan the array
        Find the insertion point with binary search, then do normal interval
        merge.
        '''
        start = bisect.bisect(intervals, newInterval)
        ans = []
        for s, e in intervals[:start] + [newInterval] + intervals[start:]:
            if ans and ans[-1][1] >= s:
                ans[-1][1] = max(e, ans[-1][1])
            else:
                ans.append([s, e])
        return ans
        '''
        2/2 Binary search both boundaries
        '''
        left = bisect_right(intervals, [newInterval[0], 0])
        if 0 <= left - 1 and newInterval[0] <= intervals[left - 1][1]:
            newInterval[0] = intervals[left - 1][0]
            newInterval[1] = max(newInterval[1], intervals[left - 1][1])
            left -= 1

        right = bisect_right(intervals, [newInterval[1], inf])
        if 0 <= right - 1 and intervals[right - 1][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[right - 1][1])

        intervals[left:right] = [newInterval]
        return intervals
