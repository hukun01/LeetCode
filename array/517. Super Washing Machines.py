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

        Why not use abs(load-target)? Because [-1, 2 ,-1] and [1, -2, 1] are different! 
        The former can be balanced with 2 steps, but the latter can be balanced with
        only 1 step! That said, giving out loads and receiving loads are different. One
        machines can at most give 1 load each step, but can receive at most 2 loads each step.
        '''
        total = sum(machines)
        if total % len(machines) != 0:
            return -1

        target = total // len(machines)
        ans = toRight = 0
        for load in machines:
            toRight += load - target
            ans = max(ans, abs(toRight), load - target)
        return ans