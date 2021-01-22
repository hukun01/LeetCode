# 517. Super Washing Machines
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        '''
        Greedy.
        The min number of moves is defined by the max throughput we ever see
        in a machine. The throughput of a machine is the total give-out load
        from left to right that passes this machine.
        Note that the give-out load can be negative, meaning the machine needs
        load.
        The max throughput is the max of total give-out load, and each single
        give-out load.
        The total give-out load is the accumulated give-out load from left
        machines to current machines, it may be negative, so we need to take
        its absolute value.
        For the single give-out load, we only consider positive load, because
        for positive load L, we need at least L steps to give it out, while
        for negative load -L, we can have less than L steps to take in loads
        from both left and right sides.

        The key is to measure the GIVE OUT load from each machine, not TAKE IN,
        because take-in can happen from both left and right, and give-out is
        unidirectional, and each give-out is counted as one move.

        Time: O(n) where n is len(machines)
        Space: O(1)

        Similar to 979. Distribute Coins in Binary Tree
        '''
        target, remainder = divmod(sum(machines), len(machines))
        if remainder != 0:
            return -1
        ans = 0
        total_give_out = 0 # total give out to the right machines
        for load in machines:
            give_out = load - target
            ans = max(ans, give_out)
            total_give_out += give_out
            ans = max(ans, abs(total_give_out))
        return ans