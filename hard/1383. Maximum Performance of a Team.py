# 1383. Maximum Performance of a Team
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        '''
        The team efficiency is dominated by the lowest efficiency,
        so we try each efficiency, from high to low, with accumulating
        total speed.
        If we need to remove people, remove the person with lowest speed.

        Similar to 857. Minimum Cost to Hire K Workers.
        '''
        people = sorted(zip(efficiency, speed), reverse=True)
        total_speed = ans = 0
        used_speeds = []
        for e, s in people:
            total_speed += s
            heappush(used_speeds, s)
            if len(used_speeds) > k:
                total_speed -= heappop(used_speeds)
            ans = max(ans, total_speed * e)

        return ans % (10 ** 9 + 7)