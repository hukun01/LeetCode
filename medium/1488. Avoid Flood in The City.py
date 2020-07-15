# 1488. Avoid Flood in The City
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        '''
        1/2 Greedy and sort.
        Scan the rains array, find the total raining days for each lake.
        Use a heap to store the closest future raining day for any lake.
        When it's a raining day, get the lake's future raining days, and
        store the next raining day of that lake.
        When it's a dry day, empty the lake at rains[closest future raining day].
        On any day, if there's any lake whose closest raining day is that day,
        then that lake has not been emptied, so there's no answer.
        '''
        lake_to_rain_days = defaultdict(deque)
        for day, lake in enumerate(rains):
            lake_to_rain_days[lake].append(day)
            
        closest = []
        ans = [-1 if r > 0 else 1 for r in rains]
        for day, lake in enumerate(rains):
            if closest and closest[0] == day:
                return []
            if lake > 0:
                rain_days = lake_to_rain_days[lake]
                rain_days.popleft()
                if rain_days:
                    heapq.heappush(closest, rain_days[0])
            else:
                if not closest:
                    continue
                ans[day] = rains[heapq.heappop(closest)]
        return ans
    
        '''
        2/2 Binary search.
        Collect the dry days, and the rained lakes.
        When a lake rains again, find the min dry day that's greater than the
        lake's previous rain day, and dry the lake (pop out that dry day).
        If no such dry day can be found, there's no answer.
        '''
        from sortedcontainers import SortedSet
        rained = dict() # { lake: day } in chrono order
        ans = [-1] * len(rains)
        dry_days = SortedSet()
        for day, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(day)
            else:
                # flood's coming. Find a dry day to empty this lake
                # search for a first dry day after the lake's previous raining day
                if lake in rained:
                    dry_day_idx = dry_days.bisect_right(rained[lake])
                    if dry_day_idx == len(dry_days):
                        return []
                    ans[dry_days[dry_day_idx]] = lake
                    dry_days.pop(dry_day_idx)
                rained[lake] = day

        for day in dry_days:
            ans[day] = 1 # can be anything in [1, 10^9]
        return ans