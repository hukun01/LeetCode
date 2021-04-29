# 1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        1/3 Difference array.

        Imagine the people at each distance, when they onboard, we add n people
        to the distance interval, when they drop off, we remove n. At the end,
        we check whether the peak traffic exceeds the capacity.
        This is where difference array helps.

        Time: O(T) where T is the range of trips.
        Space: O(T)

        Same as 370. Range Addition.
        '''
        people = [0] * (1 + max(e for _, _, e in trips))
        for n, s, e in trips:
            people[s] += n
            people[e] -= n
        return max(accumulate(people)) <= capacity
        '''
        2/3 Sort + Priority queue.

        If T is huge, 1/2 may not be the best option, in this case, we sort
        the trips by start and end time, and use a heap to track the used
        capacity and when it will be restored. This is similar to the scan
        logic in 218. The Skyline Problem.

        Time: O(n log(n)) where n is len(trips)
        Space: O(n)
        '''
        passengers = []
        for n, s, e in sorted(trips, key=lambda t: (t[1], t[2])):
            while passengers and passengers[0][0] <= s:
                _, restored_capacity = heappop(passengers)
                capacity += restored_capacity

            capacity -= n
            if capacity < 0:
                break
            heappush(passengers, (e, n))
        return capacity >= 0
        '''
        3/3 Collect events and line sweep.

        This approach is similar to 1/3, except that this can handle arbitrary
        value range. We collect start and end interval changes in the hashmap,
        and scan through hashmap's keys (interval boundaries), and accumulate
        each values, just like the logic in 1/3.

        Time: O(n log(n))
        Space: O(n)
        '''
        events = Counter()
        for num, s, e in trips:
            events[s] += num
            events[e] -= num

        return max(accumulate(v for _, v in sorted(events.items()))) <= capacity