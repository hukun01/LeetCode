# 1094. Car Pooling
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        1/2 Difference array.

        Imagine the people at each distance, when they onboard, we add n people
        to the distance interval, when they drop off, we remove n. At the end,
        we check whether the peak traffic exceeds the capacity.
        This is where difference array helps.

        Time: O(T) where T is the range of trips.
        Space: O(T)

        Same as 370. Range Addition.
        '''
        people = [0] * 1001
        for n, s, e in trips:
            people[s] += n
            people[e] -= n
        return max(accumulate(people)) <= capacity
        '''
        2/2 Sort + Priority queue.

        If T is huge, 1/2 may not be the best option, in this case, we sort
        the trips by start and end time, and use a heap to track the used
        capacity and when it will be restored. This is similar to the scan
        logic in 218. The Skyline Problem.

        Time: O(n log(n)) where n is len(trips)
        Space: O(n)
        '''
        off = []
        for n, s, e in sorted(trips, key=lambda t: (t[1], t[2])):
            while off and off[0][0] <= s:
                _, restored_capacity = heappop(off)
                capacity += restored_capacity
            if capacity < n:
                return False
            capacity -= n
            heappush(off, (e, n))
        return True