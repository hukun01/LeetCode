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
        Similar to merge intervals, we need to chain up all interval list, sort by start time,
        and start merging. Note that we only need to keep the last interval.
        '''
        lastInterval = None
        ans = []
        for s in sorted(itertools.chain(*schedule), key=lambda x: x.start):
            if lastInterval is not None and s.start <= lastInterval.end:
                lastInterval.end = max(lastInterval.end, s.end)
            else:
                if lastInterval is not None:
                    ans.append(Interval(lastInterval.end, s.start))
                lastInterval = s
        return ans