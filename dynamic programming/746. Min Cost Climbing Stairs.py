class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        This is the same as the 70. Climbing Stairs, but the trick is to return the min of 
        the cost at (i-2th stair, i-1th stair), because both a and b reaches the top.
        """
        # a denotes the cost to start from the i-2th stair; 
        # b denotes the cost to start from the i-1th stair
        a, b = cost[0], cost[1]
        for c in cost[2:]:
            x = c + min(a, b) # can only climb after paying the cost!
            a, b = b, x
        return min(a, b)