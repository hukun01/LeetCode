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

        Time: O(n log(n)) where n is len(events)
        Space: O(n)
        '''
        events.sort()
        ans = 0
        day = 1
        available_events = []

        i = 0
        while i < len(events) or available_events:
            while i < len(events) and events[i][0] <= day:
                heappush(available_events, events[i][1])
                i += 1

            while available_events:
                current_event_end = heappop(available_events)
                if current_event_end >= day:
                    ans += 1
                    break
            day += 1

        return ans