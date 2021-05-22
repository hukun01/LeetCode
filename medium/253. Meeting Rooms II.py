# 253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        1/2 Sort the intervals by their start time.
        Iterate through the intervals, use a heap to keep track of the
        overlapped meetings. 
        At every iteration, pop out all the ends that are less than the current
        start time, because those meetings already ends when the current one
        starts. We don't need extra rooms for those meetings.
        The max number of overlapped meetings, which is len(heap), will be the
        number of rooms we need.

        Time: O(n log(n)) where n is len(intervals).
        Space: O(n)

        Similar to the scan logic in 218. The Skyline Problem, and
        1235. Maximum Profit in Job Scheduling, and 1094. Car Pooling.
        '''
        rooms = 0
        heap = []
        for s, e in sorted(intervals):
            while heap and heap[0] <= s:
                heappop(heap)
            heappush(heap, e)
            rooms = max(rooms, len(heap))
        return rooms
        '''
        2/2
        Line sweep. Same as 1094. Car Pooling.

        Time: O(n log(n)) where n is len(intervals).
        Space: O(n)
        '''
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e, -1))

        cur = ans = 0
        for e, d in sorted(events):
            cur += d
            ans = max(ans, cur)

        return ans