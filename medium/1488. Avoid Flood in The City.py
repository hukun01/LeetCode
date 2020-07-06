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
        
        '''
        from sortedcontainers import SortedSet
        n = len(rains)
        res = [-1] * n
        rained = dict() # { lake: day } in chrono order
        dry_days = SortedSet()

        for day, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(day)
            else:
                if lake in rained: # flood's coming. Find a dry day to empty this lake
                    # search for a first dry day after the lake's previous raining day
                    min_dry_day_idx = dry_days.bisect_right(rained[lake])
                    if min_dry_day_idx == len(dry_days):
                        return []
                    res[dry_days[min_dry_day_idx]] = lake
                    dry_days.pop(min_dry_day_idx)
                rained[lake] = day

        for day in dry_days:
            res[day] = 1 # can be anything in [1, 10^9]
        return res