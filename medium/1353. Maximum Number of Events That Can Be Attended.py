# 1353. Maximum Number of Events That Can Be Attended
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        Greedy + Heap.
        Sort the events by start time. For each day d, find out all the events
        that starts before d, among those available events, pick the earliest
        ending one.
        Note that the earliest ending event may not be compatible if it ends
        earlier than d, so we need to skip it.
        Also, if there's not available events at the beginning, we should set
        d = events[i][0] otherwise there would be no events being added in the
        next step.

        Time: O(n log(n)) where n is len(events)
        Space: O(n)
        '''
        events.sort()
        available_events = []
        ans = 0
        day = 1
        i = 0
        while i < len(events) or available_events:
            if not available_events:
                day = events[i][0]

            while i < len(events) and events[i][0] <= day:
                heappush(available_events, events[i][1])
                i += 1

            heappop(available_events)
            day += 1
            ans += 1
            while available_events and available_events[0] < day:
                heappop(available_events)

        return ans