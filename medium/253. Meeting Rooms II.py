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
        1235. Maximum Profit in Job Scheduling.
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
        Decompose the intervals into start times and end times, and scan them
        based on time.

        Sort the starts and ends in two arrays, scan through starts array. 

        When we see a start time, we have a new meeting with newStart, 
        if newStart < currentEnd, we need a new room, because the other meeting 
        with currentEnd has not ended; 

        if newStart >= currentEnd, that means the meeting with currentEnd has
        ended, we have one empty room, the new meeting can happen in this empty
        room, so no need to increase the total number of rooms, and we will go
        to the next room start time. Also, as newStart >= currentEnd, the time
        has passed, so we need to move to the next end time.

        Time: O(n log(n)) where n is len(intervals).
        Space: O(n)
        '''
        ans = cur = 0
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        end_idx = 0
        for s in starts:
            if s < ends[end_idx]:
                cur += 1
            else:
                end_idx += 1
            ans = max(ans, cur)
        return ans