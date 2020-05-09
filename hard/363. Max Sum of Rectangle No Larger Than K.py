# 363. Max Sum of Rectangle No Larger Than K
from sortedcontainers import SortedSet
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        '''
        Kadane's algorithm applied on 2D.
        '''
        m = matrix
        if not m or not m[0]:
            return 0
        R, C = len(m), len(m[0])
        ans = -math.inf
        for left in range(C):
            sums = [0] * R
            for right in range(left, C):
                for i in range(R):
                    sums[i] += m[i][right]
                
                s = SortedSet()
                s.add(0)
                currSum = 0
                for sum1 in sums:
                    currSum += sum1
                    idx = s.bisect_left(currSum - k)
                    if idx != len(s):
                        ans = max(ans, currSum - s[idx])
                        if ans == k:
                            return k
                    s.add(currSum)
        return ans