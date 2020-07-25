# 1524. Number of Sub-arrays With Odd Sum
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        DP.
        Let f[i] be the number of sums of subarrys that end with arr[:i],
        to track f[i], we need to maintain both the number of odd sums,
        and the number of even sums.
        Adding an odd number to odd sums makes the same number
        of even sums;
        Adding an odd number to even sums makes the same number
        of odd sums, and one new odd sum which is the new odd itself.
        Similar logic applies to how adding an even number affects
        the number of even sums.
        '''
        MOD = 10 ** 9 + 7

        ans = odd = even = 0
        for a in arr:
            if a % 2 == 0:
                even += 1
            else:
                even, odd = odd, even + 1
            ans += odd
            ans %= MOD
        return ans