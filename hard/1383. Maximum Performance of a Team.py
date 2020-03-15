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
        engineers = sorted(zip(efficiency, speed), reverse=True)
        ans = 0
        totalSp = 0
        mySpeed = []
        for e, s in engineers:
            heapq.heappush(mySpeed, s)
            totalSp += s
            if len(mySpeed) > k:
                totalSp -= heapq.heappop(mySpeed)
            ans = max(ans, totalSp * e)
        return ans % (10 ** 9 + 7)