# 134. Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        Notice that:
        1. We can't start at i if the current remainig gas (gas[i] - cost[i]) < 0,
        so we should try i + 1 as starting point, and reset current gas to be 0;
        2. If the total gas - total cost is non-negative, then it must be possible
        to do a round trip. (Can use proof of contradiciton).
        
        Hence, the last index we try would be the answer if the total gas-cost >= 0.

        Similar to 517. Super Washing Machines, and
        979. Distribute Coins in Binary Tree
        '''
        totalGas = tank = 0
        start = 0
        for i in range(len(gas)):
            totalGas += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                # at any station, if the tank runs out of gas, we can't start from that station.
                # try to start from the next station.
                start = i + 1
                tank = 0
        return start if totalGas >= 0 else -1