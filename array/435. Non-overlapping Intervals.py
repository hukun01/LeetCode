class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Similar to Interval Scheduling problem that asks about the max number of non-overlapping intervals.
        In this problem, the interval that ends first is the most preferrable to keep, we need to remove 
        all the bad ones that overlap with this interval, then we can move to the next interval.
        '''
        end = -float('inf')
        erased = 0
        for i in sorted(intervals, key=lambda i: i[1]):
            if i[0] >= end:
                end = i[1]
            else:
                erased += 1
        return erased