# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Find the insertion point with binary search, then do normal
        interval merge.
        '''
        start = bisect(intervals, newInterval)
        ans = []
        for s, e in intervals[:start] + [newInterval] + intervals[start:]:
            if not ans or s > ans[-1][1]:
                ans.append([s, e])
            else:
                ans[-1][1] = max(ans[-1][1], e)
        return ans