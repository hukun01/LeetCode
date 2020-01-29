# 517. Super Washing Machines
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        '''
        Two parts:
        1. Ensure there is a solution by checking the total % len(machines) == 0.
        2. For each machine from left to right, the max number of dresses that need 
        to be passed through a machine is 
        max(max(throughput of every washer), max(give out of every washer)).
        This total number can be negative, meaning that we need to get dresses 
        from machines on the right, in that case we need to get the abs() number.

        The max total number of passed dresses is the minimum number of moves.
        Similar to 979. Distribute Coins in Binary Tree
        '''
        total = sum(machines)
        if total % len(machines) != 0:
            return -1

        target = total // len(machines)
        ans = toRight = 0
        for m in machines:
            toRight += m - target
            ans = max(ans, abs(toRight), m - target)
        return ans