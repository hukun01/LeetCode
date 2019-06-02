class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Sort the starts and ends in two arrays, scan through starts array.

        When we see a start time, we have a new meeting with newStart,
        if newStart < currentEnd, we need a new room, because the other meeting
        with currentEnd has not ended;

        if newStart >= currentEnd, that means the meeting with currentEnd has ended,
        we have one empty room, the new meeting can happen in this empty room, so no need
        to increase the total number of rooms. Also, as newStart >= currentEnd, the time
        has passed, so we need to move to the next end time.
        '''
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        endIdx = 0
        rooms = 0
        for s in starts:
            if s < ends[endIdx]:
                rooms += 1
            else:
                endIdx += 1
            
        return rooms