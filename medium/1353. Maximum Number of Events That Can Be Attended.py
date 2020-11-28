# 1353. Maximum Number of Events That Can Be Attended
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        1/2
        Sort the events, for each day d, find out all the events that starts before d,
        then exclude all the events that ends before d. Use a heap to store the ends so
        we can remove the ends quickly.
        Now the heap only has events that are ongoing, and we pop the one that ends earliest.
        '''
        minS = min(e[0] for e in events)
        maxE = max(e[1] for e in events)
        ans = 0
        heap = []
        events.sort(reverse=True)
        for start in range(minS, maxE + 1):
            while events and events[-1][0] <= start:
                heappush(heap, events.pop()[1])
            while heap and heap[0] < start:
                heappop(heap)
            if heap:
                heappop(heap)
                ans += 1
        return ans
        '''
        2/2 Sort the events by end time then start time.
        Keep a set of attending days, iterate through the events,
        if start is not in the set, we can attend an event on that day.
        If start is in the set, we find the next day that we can use to
        attend this event.
        Then the number of events would be the size of days set.
        '''
        days = set()
        ans = 0
        for s, e in sorted(events, key=lambda e: (e[1], e[0])):
            if s not in days:
                days.add(s)
            else:
                i = s + 1
                while i in days and i <= e:
                    i += 1
                if i <= e:
                    days.add(i)
        
        return len(days)