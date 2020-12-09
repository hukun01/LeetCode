# 759. Employee Free Time
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        '''
        Array.
        Counting free time directly is not straightforward, instead, count the
        overall working time, and the common free time is the gap between each
        working intervals.
        Similar to 56. Merge Intervals, we need to chain up all interval list,
        sort by start time, and start merging. Note that we only need to keep
        the last interval.

        Time: O(n) where n is len(schedule)
        Space: O(n) to store output
        '''
        last_interval = None
        ans = []
        for s in sorted(itertools.chain(*schedule), key=lambda x: x.start):
            if last_interval is not None and s.start <= last_interval.end:
                last_interval.end = max(last_interval.end, s.end)
            else:
                if last_interval is not None:
                    ans.append(Interval(last_interval.end, s.start))
                last_interval = s
        return ans