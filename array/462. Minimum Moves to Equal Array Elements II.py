# 462. Minimum Moves to Equal Array Elements II
import statistics
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        From two sets of points, the median is the point where we can reach both sides in the minimum total distance.
        '''
        m = int(statistics.median(nums))
        return sum(abs(n - m) for n in nums)