class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This is the same as the 746. Min Cost Climbing Stairs, just without cost.
        """
        # 'a' denotes the #ways to start from the i-2th stair;
        # 'b' denotes the #ways to start from the i-1th stair.
        if n <= 2:
            return n
        a = b = 1
        for _ in range(2, n):
            a, b = b, a + b
        return a + b