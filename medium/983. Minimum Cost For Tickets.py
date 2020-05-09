# 983. Minimum Cost For Tickets
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        1/2 DP.
        Let f[i] be the min cost for the days[:i]
        f[0] = 0
        f[i] = min(f[i], f[i - j] + cost[x] for j, x in [(1, 0), (7, 1), (30, 2)])
        '''
        f = [math.inf] * (len(days) + 1)
        f[0] = 0
        for i in range(1, len(days) + 1):
            f[i] = f[i-1] + min(costs) # buy one ticket at least
            for j in range(i-1, 0, -1):
                if days[i-1] - days[j-1] < 7:
                    f[i] = min(f[i], f[j-1] + costs[1])
                if days[i-1] - days[j-1] < 30:
                    f[i] = min(f[i], f[j-1] + costs[2])
                else:
                    break
        return f[-1]
        '''
        2/2 DP.
        Let f[i] be the min cost for the first i days in the year, including the days without travel.
        f[i] = f[i-1] if day i is not in the plan;
        f[i] = min(f[i - x] + cost for x, cost in costs)
        '''
        lastDay = days[-1]
        f = [0] * (lastDay + 1)
        days = set(days)
        costs = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
        for d in range(1, lastDay + 1):
            if d not in days:
                f[d] = f[d-1]
            else:
                f[d] = min(f[max(0, d - day)] + cost for day, cost in costs)
        return f[-1]