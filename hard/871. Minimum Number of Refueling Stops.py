# 871. Minimum Number of Refueling Stops
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        '''
        Greedy + heap.

        We keep going by skipping every stations as long as we have fuel. While
        the tank is negative, we go back in time and find the station with the
        most fuel and take that. To track the past fuels we use a max heap.
        Note that we need to add [target, 0] to the stations.

        Time: O(n log(n)) where n is len(stations)
        Space: O(n)

        Similar to 630. Course Schedule III
        '''
        past_fuels = []
        tank = startFuel
        prev_pos = 0
        for pos, fuel in stations + [[target, 0]]:
            tank -= pos - prev_pos
            prev_pos = pos
            while past_fuels and tank < 0:
                tank -= heappop(past_fuels)
            if tank < 0:
                return -1
            heappush(past_fuels, -fuel)
        return len(stations) + 1 - len(past_fuels)