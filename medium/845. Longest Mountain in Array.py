# 845. Longest Mountain in Array
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        '''
        Array.
        We count the number of increasing and decreasing points while going
        through the array, per the definition of mountain, we can only collect
        results when we have both inc and dec. And we need to reset inc and/or
        dec when we switch to a new mountain.
        The key is to identify the difference between the number of
        inc/dec points vs the length of the subarray.

        Time: O(n) where n is len(A).
        Space: O(1)
        '''
        ans = inc = dec = 0
        for i in range(1, len(A)):
            curr = A[i]
            prev = A[i-1]
            if curr > prev:
                if dec > 0:
                    inc = 0
                dec = 0
                inc += 1
            elif curr < prev:
                dec += 1
            else:
                dec = inc = 0

            if inc > 0 and dec > 0:
                ans = max(ans, inc + dec + 1)

        return ans