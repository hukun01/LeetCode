# 363. Max Sum of Rectangle No Larger Than K
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        '''
        Kadane's algorithm applied on 2D.
        '''
        from sortedcontainers import SortedSet
        m = matrix
        if not m or not m[0]:
            return 0
        R, C = len(m), len(m[0])
        ans = -inf
        for left in range(C):
            sums = [0] * R
            for right in range(left, C):
                for r in range(R):
                    sums[r] += m[r][right]

                s = SortedSet()
                s.add(0)
                cur_sum = 0
                for sum1 in sums:
                    cur_sum += sum1
                    idx = s.bisect_left(cur_sum - k)
                    if idx != len(s):
                        ans = max(ans, cur_sum - s[idx])
                        if ans == k:
                            return k
                    s.add(cur_sum)
        return ans