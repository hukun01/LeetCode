# 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1/2
        Similar to Interval Scheduling problem that asks about the max number
        of non-overlapping intervals.
        In this problem, the interval that ends first is the most preferrable
        to keep, we need to remove all the bad ones that overlap with this
        interval, then we can move to the next interval.
        '''
        end = -float('inf')
        erased = 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if end <= s:
                end = e
            else:
                erased += 1
        return erased
        '''
        2/2
        Another way to model this problem is to see it as "Given a collection
        of intervals, find the maximum number of intervals that are
        non-overlapping", and the rest is what we need to remove.
        '''
        end = -float('inf')
        nonOverlap = 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if end <= s:
                end = e
                nonOverlap += 1
        return len(intervals) - nonOverlap