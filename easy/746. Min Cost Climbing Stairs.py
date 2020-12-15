class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        DP.
        This is the same as the 70. Climbing Stairs, but the trick is to
        return the min of the cost at (i-2th stair, i-1th stair), because both
        f1 and f2 reaches the top. Note f1 is f[i-1] and f2 is f[i-2] where
        f[i] is the min cost to climb to i-th stair.

        Time: O(n) where n is len(cost)
        Space: O(1)
        """
        f1 = cost[0]
        f2 = 0
        for c in cost[1:]:
            fi = min(f1, f2) + c
            f1, f2 = fi, f1
        return min(f1, f2)